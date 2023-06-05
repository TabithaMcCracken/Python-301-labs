# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'
line = 1

try:

    with open (file_name, "r") as my_file:
        contents = my_file.readlines()[line-1]
        contents = int(contents)

except IOError:
    print("This file does not exist.")

except ValueError:
    print("This isn't a number.")

else:
    print(f"The number is: {contents}")
    sq_value = contents * contents
    print(f"{contents} squared is : {sq_value}")