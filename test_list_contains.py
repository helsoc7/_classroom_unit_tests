import unittest
import os
from list_contains import list_contains

class Test(unittest.TestCase):
    def test_list_contains(self):
        self.assertTrue(list_contains([1, 2, 3], 2))
        self.assertFalse(list_contains([1, 2, 3], 4))
        self.assertFalse(list_contains([], 1))

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
