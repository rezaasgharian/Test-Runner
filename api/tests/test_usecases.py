from collections import OrderedDict

from django.test import TestCase

from api.models import TestFilePath, TestEnvironment
from api.usecases import get_assets


class TestGetAssets(TestCase):
    def setUp(self) -> None:
        TestFilePath.objects.all().delete()
        TestEnvironment.objects.all().delete()

    def test_empty_models(self):
        self.assertEqual(
            {'available_paths': [], 'test_envs': []},
            get_assets()
        )

    def test_models_data_initialized(self):
        path = TestFilePath.objects.create(path='path1')
        env = TestEnvironment.objects.create(name='env1')
        path_dict = OrderedDict([('id', path.id), ('path', path.path)])
        env_dict = OrderedDict([('id', env.id), ('name', env.name)])
        data = get_assets()
        self.assertIn('available_paths', data)
        self.assertIn('test_envs', data)
        self.assertEqual(1, len(data['available_paths']))
        self.assertEqual(1, len(data['test_envs']))
        self.assertEqual(path_dict, data['available_paths'][0])
        self.assertEqual(env_dict, data['test_envs'][0])
