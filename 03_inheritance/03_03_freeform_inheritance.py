# Done
# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Restaurant:
    """Restaurants"""
    def __init__(self, name, region, to_go, price, meal) -> None:
        self.name = name
        self.region = region # Part of the world where food is from
        self.to_go = to_go # Y or N
        self.price = price # 1-$, 2-$$, 3-$$$
        self.meal = meal # breakfst, lunch or dinner

    def __str__(self) -> str:
        return f"{self.name} {self.region} {self.drive_thru} {self.to_go} {self.price} {self.meal}"

class FastFood(Restaurant):
    def __init__(self, name, region, to_go, meal, price=1, drive_thru=True) -> None:
        super().__init__(name, region, to_go, price, meal)
        self.drive_thru = drive_thru

class BurgerJoint(FastFood):
    def __init__(self, name, to_go, meal, burger_meat, region = "American", price=1, drive_thru=True) -> None:
        super().__init__(name, region, to_go, meal, price, drive_thru)
        self.burger_meat = burger_meat

class Gourmet(Restaurant):
    def __init__(self, name, region, to_go, meal, valet, price=3) -> None:
        super().__init__(name, region, to_go, price, meal)
        self.valet = valet


mcdonalds = FastFood(
    name= "McDonalds", 
    region= "American", 
    to_go=True,
    meal= ["breakfast", "lunch", "dinner"])

in_n_out = BurgerJoint(
    name= "In N Out",
    to_go= True,
    meal = ["lunch", "dinner"],
    burger_meat = ["beef", "vegetarian", "buffalo"])

la_loma = Gourmet(
    name = "La Loma",
    region= "Mexican",
    to_go= True,
    meal = ["breakfast", "lunch", "dinner"],
    valet= True)

print(mcdonalds.price)
print(la_loma.valet)
print(in_n_out.burger_meat)
print(in_n_out.region)