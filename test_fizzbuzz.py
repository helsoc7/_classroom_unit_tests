import unittest
import os
from fizzbuzz import fizzbuzz

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), "1, 2, Fizz")
        self.assertEqual(fizzbuzz(5), "1, 2, Fizz, 4, Buzz")
        self.assertEqual(fizzbuzz(15), "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz")
