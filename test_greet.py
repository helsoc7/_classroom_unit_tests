import unittest
import os
from greet import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Max"), "Hallo, Max!")
        self.assertEqual(greet("Anna"), "Hallo, Anna!")
        self.assertEqual(greet(""), "Hallo, !")

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
