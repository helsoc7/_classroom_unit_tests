import unittest
import os
from leap_year_checker import is_leap

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = "leap_year_checker.py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_is_leap(self):
        self.assertTrue(is_leap(2000))
        self.assertFalse(is_leap(1900))
        self.assertTrue(is_leap(2016))
        self.assertFalse(is_leap(2019))

