import unittest
import os
from find_position import find_position

class Test(unittest.TestCase):
    def test_find_position(self):
        self.assertEqual(find_position([1, 2, 3], 2), 1)
        self.assertEqual(find_position([1, 2, 3], 4), -1)
        self.assertEqual(find_position([], 1), -1)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
