import unittest
import os
from sum_list import sum_list

class TestSumList(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4]), 10)
        self.assertEqual(sum_list([-1, -2, -3, -4]), -10)
        self.assertEqual(sum_list([0, 0, 0]), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
