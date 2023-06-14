# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
import mymath

class TestMyMath(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(mymath.subtract_divide(30,20,10), 3)

class TestMyMath2(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(mymath.subtract_divide(30,20,20), 3)

if __name__ == "__main__":
    unittest.main()