from django.test import TestCase

from api.models import TestRunRequest


class TestExtendedEnum(TestCase):

    def test_get_as_tuple(self):
        self.assertEqual(
            [
                ('SUCCESS', 'SUCCESS'),
                 ('RUNNING', 'RUNNING'),
                 ('FAILED', 'FAILED'),
                 ('CREATED', 'CREATED'),
                 ('RETRYING', 'RETRYING'),
                 ('FAILED_TO_START', 'FAILED_TO_START')
            ],
            TestRunRequest.StatusChoices.get_as_tuple()
        )
