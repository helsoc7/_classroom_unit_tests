import unittest
import os
from max_of_two import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_max_of_two(self):
        self.assertEqual(max_of_two(3, 5), 5)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(-1, 1), 1)
        self.assertEqual(max_of_two(0, 0), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
