import unittest
import os
from find_max import find_max

class TestFindMax(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(3, 5), 5)
        self.assertEqual(find_max(10, 7), 10)
        self.assertEqual(find_max(-1, -5), -1)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
