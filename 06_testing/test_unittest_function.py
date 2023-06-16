import unittest_function
import unittest
from unittest_function import CustomNegativeError
from unittest_function import CustomZeroDivsionError
from unittest_function import gas_mileage_calculator

class TestUnittest_function (unittest.TestCase):
    # def test_function_throws_exception(self):
    #     self.assertRaises(AssertionError, gas_mileage_calculator, 100, 90, 5)

    def test_function_throws_custom_negative_error (self):
        self.assertRaises(CustomNegativeError, gas_mileage_calculator, 100, 200, 0)

    def test_function_throws_zero_division_error (self):
        self.assertRaises(CustomZeroDivsionError, gas_mileage_calculator, 100, 100, 0)

    # def test_mileage_not_negative(self):
    #     self.assertEqual(unittest_function.gas_mileage_calculator(100,50,5), 20)

    # def test_zero_division(self):
    #     self.assertEqual(unittest_function.gas_mileage_calculator(100,200,0), 0)


if __name__ == "__main__":
    unittest.main()
