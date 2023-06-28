# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

class CustomZeroDivsionError(Exception):
    pass

class CustomNegativeError(Exception):
    pass

def gas_mileage_calculator(starting_miles, finishing_miles, gallons_of_gas):

    try:
        miles = finishing_miles-starting_miles
        if miles <= 0 :
            raise CustomNegativeError("The mileage must be greater than 0.")
        
        gas_mileage = miles / gallons_of_gas
        # assert gas_mileage > 0
        return gas_mileage
    
    except ZeroDivisionError:
        raise CustomZeroDivsionError (f"We cannot calculate your gas mileage unless you put in gas.")
    # except AssertionError :
    #     print("The miles drive is negative or zero.")

if __name__ == "__main__":

    starting_miles = int(input("What was your starting mileage?"))
    finishing_miles = int(input("What was your ending mileage?"))
    gallons_of_gas = int(input("How many gallons of gas did you put in the car at the end?"))

    gas_mileage = gas_mileage_calculator(starting_miles, finishing_miles, gallons_of_gas)

    if gas_mileage:
        print(f"You're gas mileage is: {gas_mileage}")