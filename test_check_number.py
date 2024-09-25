import unittest
import os
from check_number import check_number

class TestCheckNumber(unittest.TestCase):
    def test_check_number(self):
        self.assertEqual(check_number(5), 'positiv')
        self.assertEqual(check_number(-3), 'negativ')
        self.assertEqual(check_number(0), 'null')

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
