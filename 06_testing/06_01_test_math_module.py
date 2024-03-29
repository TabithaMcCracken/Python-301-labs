# Done
# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.


import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), None) #Should fail

    def test_gcd_gets_greatest_common_divisory(self):
        self.assertEqual(math.gcd(1206,765), 9)


if __name__ == "__main__":
    unittest.main()