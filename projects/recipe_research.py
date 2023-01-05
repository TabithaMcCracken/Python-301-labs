# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

# Steps
# Pass ingredients into soup
# Add them together
# Open a search for recipes with those ingredients

import webbrowser


class Ingredient():
    """Takes Ingredients and opens a Wikipedia page about that ingredient"""

    def __init__ (self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        url = "https://en.wikipedia.org/wiki/" + self.name
        webbrowser.open_new_tab(url)
        return url

    def __str__(self) -> str:
        return f"{self.name} {self.amount}"

class Spice(Ingredient):
    """Takes spices"""
    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste
    
class Soup():
    """Finds a soup recipe with user given ingredients"""

    def __init__(self, soup_ing) -> None:
        self.soup_ing = soup_ing

    def cook(self):
        # Create list of ingredients
        ingredients = ""
        for ingredient in self.soup_ing: ## or .soup_ing
            ingredients += ingredient.name + "+" # This is adding the name and the amount
            print(ingredients)

        # Get recipes from google with items in the list
        url = "https://www.google.com/search?q=soup+recipe+" + ingredients
        webbrowser.open_new_tab(url)
        return url

    def __str__(self) -> str:
        return f"{self.soup_ing}"

ingredient_list = []
name_list = []
while True:
    response = str(input("Would you like to add an ingredient to your list?"))
    if response == "yes":
        ingredient_name = input("What is your ingredient?")
        ingredient_amount = input("How much do you have?")
        ingredient_list.append(Ingredient(ingredient_name, ingredient_amount))
        print("Here is your ingredient list: ")
        for item in ingredient_list:
            print(item.name, item.amount)

    else:
        # for item in ingredient_list:
        #    name_list.append(item)
        print(ingredient_list)
        soup_ingredients = Soup(ingredient_list)
        soup_ingredients.cook()
        break

c = Ingredient("carrot", 2)
p = Ingredient("potato", 3)
ch = Ingredient("chicken", 1)
s = Spice("salt", 1, "salty")
# soup_ingredients = Soup([c.name, p.name, ch.name, s.name])
# soup_ingredients.cook()