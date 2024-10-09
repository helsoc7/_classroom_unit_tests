import unittest
import os
from string_length import string_length

class Test(unittest.TestCase):
    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length("Python"), 6)
        self.assertEqual(string_length(""), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
