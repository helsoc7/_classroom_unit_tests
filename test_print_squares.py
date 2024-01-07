import unittest
import os
from print_squares import print_squares

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = "print_squares.py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_print_squares(self):
        self.assertEqual(print_squares(3), [0, 1, 4])
        self.assertEqual(print_squares(5), [0, 1, 4, 9, 16])
