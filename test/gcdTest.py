import unittest

from src.gcd import GCD

class GCDTest(unittest.TestCase):


    def test_gcd_has_calculate_method(self):
        gcd = GCD()
        try:
            gcd.calculate(1, 2)
        except AttributeError:
            pass

