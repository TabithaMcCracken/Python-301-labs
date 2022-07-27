# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Vehicle:
    """Models basic car descriptions."""

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def change_max_speed(self, max_speed):
        self.max_speed += 5
        print(f"Your max speed is now: {self.max_speed}")

    def __str__(self):
        return f"{self.model} {self.year} {self.max_speed}"

    def __repr__(self):
        return f"Vehicle(model={self.model}, year={self.year}, max_speed={self.max_speed})"


customer_vehicle1 = Vehicle("Honda", 2010, 140)
customer_vehicle2 = Vehicle("Ford", 2020, 160)


print(customer_vehicle1)
customer_vehicle1.change_max_speed(Vehicle.change_max_speed)
customer_vehicle2.change_max_speed(Vehicle.change_max_speed)