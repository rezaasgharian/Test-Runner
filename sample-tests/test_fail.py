from time import sleep

from django.test import TestCase


class TestSuccess(TestCase):

    def setUp(self) -> None:
        sleep(2)

    def test_1(self):
        self.assertEqual(1, 2)

    def test_2(self):
        self.assertEqual(1, 2)

    def test_4(self):
        self.assertEqual(1, 2)

    def test_3(self):
        self.assertEqual(1, 2)

    def test_5(self):
        self.assertEqual(1, 2)

    def test_6(self):
        self.assertEqual(1, 2)

    def test_7(self):
        self.assertEqual(1, 2)
