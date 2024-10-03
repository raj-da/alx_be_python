import unittest
from simple_calculator import SimpleCalculator


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(10, 5), 15)
        self.assertEqual(SimpleCalculator.add(10, -5), 5)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(10, 5), 5)
        self.assertEqual(SimpleCalculator.subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(10, 5), 50)
        self.assertEqual(SimpleCalculator.multiply(10, -5), -50)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(10, 5), 2)
        self.assertEqual(SimpleCalculator.divide(5, 10), 0.5)
        self.assertEqual(SimpleCalculator.divide(10, 5), None)
        