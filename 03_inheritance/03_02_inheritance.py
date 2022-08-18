# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?


class Movie:
    """Movies"""
    def __init__ (self, title, year):
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} {self.year}"

    
class ActionMovie (Movie):
    """Action Movies"""

    def __init__(self, title, year, pg=13):
        super().__init__(title, year)
        self.pg = pg


m = ActionMovie("Karate Kid", 1981)

print (m.pg)