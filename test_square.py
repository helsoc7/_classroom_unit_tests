import unittest
import os
from square import square

class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(0), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
