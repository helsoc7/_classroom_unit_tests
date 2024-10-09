import unittest
import os
from sum_even_numbers import sum_even_numbers

class Test(unittest.TestCase):
    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_even_numbers([7, 9, 11]), 0)
        self.assertEqual(sum_even_numbers([0, 2, 4]), 6)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
