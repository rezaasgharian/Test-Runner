from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.core.files.temp import NamedTemporaryFile
from django.core import files


class TestUploadFile(TestCase):
    def setUp(self) -> None:
        self.temp_file = NamedTemporaryFile(delete=True)
        self.text_temp_file = files.File(self.temp_file, name="file.txt")
        self.python_temp_file = files.File(self.temp_file, name="file.py")

        self.url = reverse('upload_file')

    def test_send_empty_file(self):
        response = self.client.post(self.url)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_send_no_python_file(self):
        data = {"file": self.text_temp_file}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_send_python_file(self):
        data = {"file": self.python_temp_file}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
