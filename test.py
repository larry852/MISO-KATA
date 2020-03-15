from unittest import TestCase

from main import Kata


class KataTest(TestCase):
    def test_number_elements_0(self):
        self.assertEqual(Kata.numberElements(""), 0, "String vacío")

    def test_number_elements_1(self):
        self.assertEqual(Kata.numberElements("0"), 1, "String con un numero")