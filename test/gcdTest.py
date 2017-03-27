import unittest

from src.gcd import GCD


class GCDTest(unittest.TestCase):
    def setUp(self):
        self.gcd = GCD()

    def test_gcd_has_calculate_method(self):
        try:
            self.gcd.calculate(1, 2)
        except AttributeError:
            pass

    def test_gcd_raises_type_error_if_no_arguments_passed(self):
        self.assertRaises(TypeError, self.gcd.calculate)

    def test_gcd_raises_type_error_if_one_argument_passed(self):
        self.assertRaises(TypeError, self.gcd.calculate, 1)

    def test_gcd_raises_type_error_if_three_arguments_passed(self):
        self.assertRaises(TypeError, self.gcd.calculate, 1, 2, 3)

    def test_gcd_raises_value_error_if_non_int_argument_passed_left(self):
        self.assertRaises(ValueError, self.gcd.calculate, 'one', 2)

    def test_gcd_raises_value_error_if_non_int_argument_passed_right(self):
        self.assertRaises(ValueError, self.gcd.calculate, 1, 'two')

    def test_gcd_raises_value_error_if_non_int_argument_passed_both(self):
        self.assertRaises(ValueError, self.gcd.calculate, 'one', 'two')

    def test_gcd_returns_int_if_both_arguments_positive(self):
        self.assertIsInstance(self.gcd.calculate(1, 2), int)
        self.assertIsInstance(self.gcd.calculate(4, 2), int)
        self.assertIsInstance(self.gcd.calculate(15, 10), int)
        self.assertIsInstance(self.gcd.calculate(42, 14), int)

    def test_gcd_returns_none_if_argument_is_negative_left(self):
        self.assertIsNone(self.gcd.calculate(-1, 2))
        self.assertIsNone(self.gcd.calculate(-4, 2))
        self.assertIsNone(self.gcd.calculate(-15, 10))
        self.assertIsNone(self.gcd.calculate(-42, 14))

    def test_gcd_returns_none_if_argument_is_negative_right(self):
        self.assertIsNone(self.gcd.calculate(1, -2))
        self.assertIsNone(self.gcd.calculate(4, -2))
        self.assertIsNone(self.gcd.calculate(15, -10))
        self.assertIsNone(self.gcd.calculate(42, -14))

    def test_gcd_returns_none_if_argument_is_negative_both(self):
        self.assertIsNone(self.gcd.calculate(-1, -2))
        self.assertIsNone(self.gcd.calculate(-4, -2))
        self.assertIsNone(self.gcd.calculate(-15, -10))
        self.assertIsNone(self.gcd.calculate(-42, -14))

    def test_gcd_returns_zero_if_argument_is_zero_left(self):
        self.assertEqual(self.gcd.calculate(0, 2), 0)
        self.assertEqual(self.gcd.calculate(0, 3), 0)
        self.assertEqual(self.gcd.calculate(0, 10), 0)
        self.assertEqual(self.gcd.calculate(0, 14), 0)

    def test_gcd_returns_zero_if_argument_is_zero_right(self):
        self.assertEqual(self.gcd.calculate(1, 0), 0)
        self.assertEqual(self.gcd.calculate(4, 0), 0)
        self.assertEqual(self.gcd.calculate(15, 0), 0)
        self.assertEqual(self.gcd.calculate(42, 0), 0)

    def test_gcd_returns_zero_if_argument_is_zero_both(self):
        self.assertEqual(self.gcd.calculate(0, 0), 0)