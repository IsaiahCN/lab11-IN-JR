import unittest
from pip._internal import cache

import calculator
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(3, 7), -4)
        self.assertEqual(sub(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(3, 3), 9)
        self.assertEqual(calculator.mul(-3, 3), -9)

    def test_divide(self):  # 3 assertions
        self.assertEqual(calculator.div(4, 2), 2)
        self.assertEqual(calculator.div(3, 3), 1)
        self.assertEqual(calculator.div(-3, 1), -3)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)
        self.assertAlmostEqual(log(4, 64), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(4), 2)
        self.assertAlmostEqual(calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


if __name__ == "__main__":
    unittest.main()