from django.conf import settings
from django.db import models

from api.utils import ExtendedEnum


class Timestampable(models.Model):
    updated_at = models.DateTimeField('date updated', auto_now=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        abstract = True


class TestFilePath(Timestampable):
    path = models.CharField(max_length=1024)
    filePath = models.FileField(upload_to='tests/',unique=True, null=True)

    def __str__(self):
        return self.path


class TestEnvironment(Timestampable):
    class StatusChoices(ExtendedEnum):
        IDLE = 'IDLE'
        BUSY = 'BUSY'
    name = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=64, choices=StatusChoices.get_as_tuple(), default=StatusChoices.IDLE.name)

    def __str__(self):
        return self.name

    def is_busy(self):
        return self.status == TestEnvironment.StatusChoices.BUSY.name

    def is_idle(self):
        return self.status == TestEnvironment.StatusChoices.IDLE.name

    def lock(self):
        if self.is_busy():
            raise RuntimeError(f'Trying to lock a busy env(id: {self.id})')
        self.status = TestEnvironment.StatusChoices.BUSY.name
        self.save()

    def unlock(self):
        if self.is_idle():
            raise RuntimeError(f'Trying to unlock an idle env(id: {self.id})')
        self.status = TestEnvironment.StatusChoices.IDLE.name
        self.save()


class TestRunRequest(Timestampable):
    class StatusChoices(ExtendedEnum):
        SUCCESS = 'SUCCESS'  # tests are done successfully
        RUNNING = 'RUNNING'  # tests are running
        FAILED = 'FAILED'  # tests are done but failed
        CREATED = 'CREATED'  # request created but not started yet
        RETRYING = 'RETRYING'  # env is busy, retrying
        FAILED_TO_START = 'FAILED_TO_START'  # after some retries, env is still busy

    requested_by = models.CharField(max_length=128)
    env = models.ForeignKey(TestEnvironment, null=False, on_delete=models.CASCADE)
    path = models.ManyToManyField(TestFilePath)
    status = models.CharField(max_length=64, choices=StatusChoices.get_as_tuple(), default=StatusChoices.CREATED.name)
    logs = models.TextField(blank=True)

    def get_command(self):
        return settings.TEST_BASE_CMD + list(self.path.all().values_list('path', flat=True))

    def mark_as_running(self):
        self.status = TestRunRequest.StatusChoices.RUNNING.name
        self.save()

    def mark_as_success(self):
        self.status = TestRunRequest.StatusChoices.SUCCESS.name
        self.save()

    def mark_as_failed(self):
        self.status = TestRunRequest.StatusChoices.FAILED.name
        self.save()

    def mark_as_retrying(self):
        self.status = TestRunRequest.StatusChoices.RETRYING.name
        self.save()

    def mark_as_failed_to_start(self):
        self.status = TestRunRequest.StatusChoices.FAILED_TO_START.name
        self.save()

    def save_logs(self, logs=None):
        if not logs:
            return
        self.logs += '\n' + logs
        self.save()


