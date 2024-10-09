import unittest
import os
from check_age import check_age

class Test(unittest.TestCase):
    def test_check_age(self):
        self.assertEqual(check_age(20), 'volljährig')
        self.assertEqual(check_age(16), 'minderjährig')
        self.assertEqual(check_age(18), 'volljährig')

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
