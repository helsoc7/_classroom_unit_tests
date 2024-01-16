import unittest
from SimpleCalculator import SimpleCalculator

class Test(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)
