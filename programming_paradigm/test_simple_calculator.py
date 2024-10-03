import unittest
from simple_calculator import SimpleCalculator


class TestCalc(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(10, -5), -50)
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 10), 0.5)
        self.assertEqual(self.calc.divide(10, 5))

    if __name__ == "__main__":
        unittest.main()
        