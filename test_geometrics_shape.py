import unittest
import os
from geometric_shapes import Shape, Circle, Rectangle

class Test(unittest.TestCase):
    def test_file_exists(self):
        file_name = "geometric_shapes.py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist")

    def test_circle_area(self):
        circle = Circle("Kreis", 5.0)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=2)

    def test_rectangle_area(self):
        rectangle = Rectangle("Rechteck", 4.0, 6.0)
        self.assertEqual(rectangle.area(), 24.0)

if __name__ == '__main__':
    unittest.main()
