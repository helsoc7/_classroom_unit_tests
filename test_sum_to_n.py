import unittest
import os
from sum_to_n import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(3), 6)
        self.assertEqual(sum_to_n(1), 1)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
