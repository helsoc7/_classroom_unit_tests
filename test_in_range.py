import unittest
import os
from in_range import in_range

class TestInRange(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(in_range(5, 1, 10), 'ja')
        self.assertEqual(in_range(11, 1, 10), 'nein')
        self.assertEqual(in_range(1, 1, 10), 'ja')
        self.assertEqual(in_range(10, 1, 10), 'ja')

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
