from time import sleep

from django.test import TestCase


class TestSuccess(TestCase):

    def setUp(self) -> None:
        sleep(2)

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_4(self):
        pass

    def test_3(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass
