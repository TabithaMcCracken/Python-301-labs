# Done
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

carrot = Ingredient("carrot", 2)
carrot.get_info()

#open_url = carrot.get_info()
#print(open_url)