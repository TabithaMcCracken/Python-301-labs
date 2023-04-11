import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
print(type(page.text))

soup = BeautifulSoup(page.text)

#links = soup.find_all('a')
#for link in links:
#    print(link['href'])

# Written as a list comprehension
# links = [link['href'] for link in soup.find_all('a')]
# print(links)


URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
print(soup.prettify())

author = soup.find("p", class_="author")
print(author.text.strip("by "))

title = soup.find("t", )