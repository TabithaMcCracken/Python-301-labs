# Done
# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class Patient_form():
    """Models a patient form"""

    def __init__(self, first_name, last_name, age, gender, weight, height, activity_level):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.activity_level = activity_level

    def calories_needed(self):
        if self.gender == "female":
            bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
            print(f"The patient's BMR (Basal Metabolic Rate) is: {bmr}")
        elif self.gender == "male":
            bmr = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
            print(f"The patient's BMR (Basal Metabolic Rate) is: {bmr}")

        if self.activity_level == "sedentary":
            amr = bmr * 1.2
        elif self.activity_level == "lightly active":
            amr = bmr * 1.375
        elif self.activity_level == "moderately active":
            amr = bmr * 1.55
        elif self.activity_level == "active":
            amr = bmr * 1.725
        elif self.activity_level == "very active":
            amr = bmr * 1.9

        return amr

    def __repr__(self):
        return f"Patient (first name: {self.first_name} last name: {self.last_name}\
            age: {self.age} gender: {self.gender} weight: {self.weight} \
            height: {self.height} activity level: {self.activity_level}"

patient1 = Patient_form("Jon", "Doe", 40, "male", 90, 182, "lightly active")

amr = patient1.calories_needed()

print(f"Your daily caloric need is: {int(amr)}")