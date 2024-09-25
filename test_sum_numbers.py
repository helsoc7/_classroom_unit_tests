import unittest
import os
from sum_numbers import sum_numbers

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4]), 10)
        self.assertEqual(sum_numbers([0, 0, 0]), 0)
        self.assertEqual(sum_numbers([-1, 1]), 0)
        self.assertEqual(sum_numbers([]), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
