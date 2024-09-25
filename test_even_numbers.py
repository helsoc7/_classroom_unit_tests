import unittest
import os
from even_numbers import even_numbers

class TestEvenNumbers(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(even_numbers([7, 9, 11]), [])
        self.assertEqual(even_numbers([0, 2, 4]), [0, 2, 4])

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
