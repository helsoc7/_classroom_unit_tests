import unittest
import os
from largest_number import largest_number

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_largest_number(self):
        self.assertEqual(largest_number([1, 2, 3, 4, 5]), 5)
        self.assertEqual(largest_number([-1, -2, -3, -4, 0]), 0)
        self.assertEqual(largest_number([50, 50, 50]), 50)
