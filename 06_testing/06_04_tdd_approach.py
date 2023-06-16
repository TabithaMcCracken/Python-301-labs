# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest

class TestMathFunctions(unittest.TestCase):
    # Adds 2 numbers together
    def test_add_function(self):
        self.assertEqual(other_file.add_nums(3,5),8)

    # Divides one number the other
    def test_divide_function(self):
        self.assertEqual(other_file.divide_nums(10,5), 2)

    # Multiplies two numbers
    def test_multiply_function(self):
        self.assertEqual(other_file.multiply_nums(5,5), 25)


# Sample functions
# def add_nums (num1, num2):
#     total = num1 + num2
#     return total

# def divide_nums (num1, num2):
#     quotient = num1 / num2
#     return quotient

# def multiply_nums (num1, num2):
#     product = num1 * num2
#     return product

