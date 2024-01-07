import unittest
import os
from conditional_actions import check_number

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = "conditional_actions.py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_check_number(self):
        self.assertEqual(check_number(3), "Weird")
        self.assertEqual(check_number(4), "Not Weird")
        self.assertEqual(check_number(18), "Weird")
        self.assertEqual(check_number(22), "Not Weird")
