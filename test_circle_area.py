import unittest
import os
from math import isclose
from circle_area import circle_area

class Test(unittest.TestCase):
    def test_circle_area(self):
        self.assertTrue(isclose(circle_area(3), 28.27, rel_tol=1e-2))
        self.assertEqual(circle_area(0), 0)
        self.assertTrue(isclose(circle_area(2), 12.57, rel_tol=1e-2))
    
    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
