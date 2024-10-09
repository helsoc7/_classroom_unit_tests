import unittest
import os
from append_to_list import append_to_list

class Test(unittest.TestCase):
    def test_append_to_list(self):
        self.assertEqual(append_to_list([1, 2, 3], 4), [1, 2, 3, 4])
        self.assertEqual(append_to_list([], 1), [1])
        self.assertEqual(append_to_list([0], 0), [0, 0])

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
