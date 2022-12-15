# Done
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
    def __init__ (self, title, year, genre, length, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.length = length #in minutes
        self.rating = rating

    def __str__(self) -> str:
        return f"{self.title} {self.year}"

    
class RomCon(Movie):
    """Romantic Comedies"""
    def __init__(self, title, year, length, rating, heart_throb, genre= "romantic comedy"):
        super().__init__(title, year, genre, length, rating)
        self.heart_throb = heart_throb

class ActionMovie (Movie):
    """Action Movies"""

    def __init__(self, title, year, genre, length, rating, franchise, pg=13):
        super().__init__(title, year, genre, length, rating)
        self.pg = pg
        self.franchise = franchise

m = ActionMovie("Karate Kid", 1981, "action", 91, "PG-13", "Karate Kid")
n = RomCon("You've Got Mail", 1998, 102, 13, "Tom Hanks")

print (m.pg)
print(n.year)