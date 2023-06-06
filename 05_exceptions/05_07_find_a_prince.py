# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

text_to_find = "Prince"

book_files = [
    "books/crime_and_punishment.txt",
    "books/war_and_peace.txt",
    "books/pride_and_prejudice.txt"
]

class PrinceException(Exception): pass

for book in book_files:
    with open (book, "r") as file:
        contents = file.read(100)

    try:
        if contents.index(text_to_find):
            raise PrinceException()
    except ValueError:
        print(f"The text '{text_to_find}' was not found in the first 100 characters.")
    except PrinceException:
        print(f"This text has the word {text_to_find} in the first 100 characters.")