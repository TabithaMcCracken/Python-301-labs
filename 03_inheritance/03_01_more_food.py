# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def expire(self):
        if self.name == "salt":
            print("Salt never expires, ask the sea!")
        else:        
            print(f"your {self.name} has expired. it's probably still good.")
            self.name = 'old' + self.name

class Vegetable(Ingredient):
    """Models a vegetable to cook with."""



c = Ingredient("carrots", 3)
p = Spice("pepper", 20, "hot")
s = Spice("salt", 200, "salty")


print(c)
print(p.taste)
