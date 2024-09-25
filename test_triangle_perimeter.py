import unittest
import os
from triangle_perimeter import triangle_perimeter

class TestTrianglePerimeter(unittest.TestCase):
    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(1, 1, 1), 3)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")
