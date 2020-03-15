from unittest import TestCase

from main import Kata


class KataTest(TestCase):

    def setUp(self):
        self.string_empty = ""
        self.string_1 = "0"
        self.string_2 = "-1, 0"

    def test_number_elements_0(self):
        self.assertEqual(Kata.numberElements(self.string_empty), 0, "String vacío")

    def test_number_elements_1(self):
        self.assertEqual(Kata.numberElements(self.string_1), 1, "String con un numero")

    def test_number_elements_2(self):
        self.assertEqual(Kata.numberElements(self.string_2), 2, "String con dos numeros")

    def test_number_elements_N(self):
        string = "0,1,2,156,564"
        self.assertEqual(Kata.numberElements(string), len(string.split(',')), "String con N numeros")

    def test_min_element_0(self):
        self.assertEqual(Kata.minElement(self.string_empty), None, "String vacío")

    def test_min_element_1(self):
        self.assertEqual(Kata.minElement(self.string_1), 0, "String con un numero")

    def test_min_element_2(self):
        self.assertEqual(Kata.minElement(self.string_2), -1, "String con dos numeros")
