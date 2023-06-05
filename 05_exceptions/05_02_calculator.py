# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.




try:
    dividend = int(input("Please enter a number:"))
    divisor = int(input("Please enter another number:"))
    print(dividend/divisor)
    
except ZeroDivisionError:
    print("You can't divide by 0")

except ValueError:
    print("You must enter a digit")
