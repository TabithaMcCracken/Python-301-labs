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

# When I print the new object, the name isn't printing, but the rest of the attributes print

# Furniture
class Furniture():
    """Basic household furniture"""

    def __init__(self, name, length, width, height, weight, material):

        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.material = material

    def floor_space(self):
        area = self.length * self.width #Measured in feet
        if area <= 4:
            floor_size = "small"
        elif area <= 16:
            floor_size = "medium"
        elif area > 16:
            floor_size = "large"
        
        return floor_size

    def lift_assist (self):
        if self.weight > 40:
            need_lift_assist = "Yes"
        else:
            need_lift_assist = "No"
        
        return need_lift_assist

    def cleaning_method (self):
        if self.material == "wood":
            method = "Clean with wood polish"
        elif self.material == "cloth":
            method = "Wipe with a damp cloth and mild soap"
        elif self.material == "leather":
            method = "Wipe with a cleaning solution of 50/50 vinegar and water"

        return method

    def __add__(self, other):
        """Combines furniture pieces in a package"""
        new_name = self.name + other.name
        new_length = self.length + other.length
        new_width = self.width + other.width
        new_height = self.height + other.height
        new_weight = self.weight + other.weight
        if self.material == other.material:
            new_material = self.material
        else:
            new_material = self.material + other.material
    
        return Furniture(name=new_name, length=new_length, width=new_width, height=new_height, weight=new_weight, material=new_material)

    def __str__(self) -> str:
        return f"{self.length} {self.width} {self.height} {self.weight} {self.material}"

# floor_space_needed = furniture1.floor_space()
# print(f"How big is this piece of furniture? {floor_space_needed}")
# how_to_clean = furniture1.cleaning_method()
# print(f"How do you clean this item? {how_to_clean}")
# lift_assist = furniture2.lift_assist()
# print(f"Is a life assist needed to move this piece of furniture? {lift_assist}")

furniture1 = Furniture("chair", 2, 2, 4, 15, "wood")
furniture2 = Furniture("table", 5, 3, 3.5, 40, "leather")
furniture_package = furniture1 + furniture2
print(furniture_package) # Doesn't print the name attribute
print(furniture_package.name)

# Shoes

class Shoes():
    def __init__(self, name, type, gender, size):
        self.name = name
        self.type = type
        self.gender = gender
        self.size = size
    
    def __str__ (self):
        return f"{self.name} {self.type} {self.gender} {self.size}"

shoe1 = Shoes("Teva", "hiking", "women's", 10)
shoe2 = Shoes("Chaco", "hiking", "women's", 9)

shoe1.type = "sandal"
print(shoe1)

shoe2.size = 5
print(shoe2)

# Desserts
class Desserts():
    """Types of Desserts"""

    def __init__(self, name, type, ) -> None:
        pass