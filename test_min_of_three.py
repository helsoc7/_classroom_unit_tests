import unittest
import os
from min_of_three import min_of_three

class Test(unittest.TestCase):
    def test_min_of_three(self):
        self.assertEqual(min_of_three(3, 4, 5), 3)
        self.assertEqual(min_of_three(10, 2, 8), 2)
        self.assertEqual(min_of_three(-1, 0, 1), -1)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
