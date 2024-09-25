import unittest
import os
from positive_and_even import positive_and_even

class TestPositiveAndEven(unittest.TestCase):
    def test_positive_and_even(self):
        self.assertEqual(positive_and_even(4), 'ja')
        self.assertEqual(positive_and_even(7), 'nein')
        self.assertEqual(positive_and_even(-2), 'nein')

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
