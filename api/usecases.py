from api.models import TestFilePath, TestEnvironment
from api.serializers import TestFilePathSerializer, TestEnvironmentSerializer


def get_assets():
    return {
        'available_paths': TestFilePathSerializer(TestFilePath.objects.all().order_by('path'), many=True).data,
        'test_envs': TestEnvironmentSerializer(TestEnvironment.objects.all().order_by('name'), many=True).data
    }
