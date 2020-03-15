from unittest import TestCase

from main import Kata


class KataTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Kata.numberElements(""), 0, "String vacio")
