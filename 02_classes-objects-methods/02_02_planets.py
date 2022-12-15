# Done
# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """Models planet info"""
    
    def __init__(self, name, gravity, moons):
        self.name = name
        self.gravity = gravity
        self.moons = moons

    def __repr__(self) -> str:
        return f"Planet (name: {self.name} gravity: {self.gravity} moons: {self.moons})"


Mars = Planet("Mars", 3.721, 2)
print(Mars)