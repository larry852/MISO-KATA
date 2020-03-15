from unittest import TestCase

from main import Kata


class KataTest(TestCase):
    def test_number_elements_0(self):
        self.assertEqual(Kata.numberElements(""), 0, "String vacío")

    def test_number_elements_1(self):
        self.assertEqual(Kata.numberElements("0"), 1, "String con un numero")

    def test_number_elements_2(self):
        self.assertEqual(Kata.numberElements("0,1"), 2, "String con dos numeros")

    def test_number_elements_N(self):
        string = "0,1,2,156,564"
        self.assertEqual(Kata.numberElements(string), len(string.split(',')), "String con N numeros")

    def test_min_element_0(self):
        self.assertEqual(Kata.minElement(""), None, "String vacío")
