# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

# Furniture
class Furniture():
    """Basic household furniture"""

    def __init__(self, name, length, width, height, weight, material, warning) -> None:

        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.material = material
        self.warning = warning

    def floor_space(self, length, width):
        area = length * width
        if area <= 4:
            floor_size = "small"
        elif area <= 16:
            floor_size = "medium"
        elif area > 16:
            floor_size = "large"
        
        return floor_size

    def lift_assist (self, weight):
        if weight > 40:
            need_lift_assist = True
        else:
            need_lift_assist = False
        
        return need_lift_assist

    def cleaning_method (self, material):
        if material == "wood":
            method = "Clean with wood polish"
        elif material == "cloth":
            method = "Wipe with a damp cloth and mild soap"
        elif material == "leather":
            method = "Wipe with a cleaning solution of 50/50 vinegar and water"

        return material

    def __add__(self, other):
        new_name = self.name + other.name
        if self.weight + other.weight > 40:
            new_warning = "This item is heavy!"
        return Furniture(name=new_name, warning=new_warning)

    def __str__(self) -> str:
        return f"{self.length} {self.width} {self.height} {self.weight} {self.material}"

 

# Shoes

# Desserts