import unittest
import os
from create_list import create_list

class TestCreateList(unittest.TestCase):
    def test_create_list(self):
        self.assertEqual(create_list(5), [1, 2, 3, 4, 5])
        self.assertEqual(create_list(0), [])
        self.assertEqual(create_list(1), [1])

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
