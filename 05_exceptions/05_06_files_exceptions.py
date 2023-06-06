# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

war_and_peace = "books/war_and_peace.txt"
crime_and_punishment = "books/crime_and_punishment.txt"
pride_and_prejudice = "books/pride_and_prejudice.txt"


# 1
with open (war_and_peace, "r") as file:
    war_contents = file.readlines()

# 2
with open (crime_and_punishment, "w") as file:
    file.write("")

# 3
file_list = [war_and_peace, crime_and_punishment, pride_and_prejudice]

for file in file_list:
    try:
        with open (file, "r") as infile:
            text = infile.readlines()
            line_text = text[0].strip()
            first_char = line_text[0]
            print(first_char)
    except IndexError:
        print(f"This file is empty: {file}")
        # for x in text:
        #     print (x[0])
        # print(''.join(line[0] for line in infile if line))
    