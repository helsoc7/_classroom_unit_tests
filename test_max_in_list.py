import unittest
import os
from max_in_list import max_in_list

class TestMaxInList(unittest.TestCase):
    def test_max_in_list(self):
        self.assertEqual(max_in_list([1, 2, 3, 4]), 4)
        self.assertEqual(max_in_list([-1, -2, -3, -4]), -1)
        self.assertEqual(max_in_list([0, 0, 0]), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
