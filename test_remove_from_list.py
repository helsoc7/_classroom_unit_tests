import unittest
import os
from remove_from_list import remove_from_list

class Test(unittest.TestCase):
    def test_remove_from_list(self):
        self.assertEqual(remove_from_list([1, 2, 3], 2), [1, 3])
        self.assertEqual(remove_from_list([1, 2, 3], 4), [1, 2, 3])
        self.assertEqual(remove_from_list([], 4), [])

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
