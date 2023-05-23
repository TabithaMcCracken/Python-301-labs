import requests
from bs4 import BeautifulSoup

""" BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)
print(type(page.text))

soup = BeautifulSoup(page.text) """

#links = soup.find_all('a')
#for link in links:
#    print(link['href'])

# Written as a list comprehension
# links = [link['href'] for link in soup.find_all('a')]
# print(links)


""" URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
print(soup.prettify())

author = soup.find("p", class_="author")
print(author.text.strip("by "))

title = soup.find("t", ) """


""" URL = "https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"

page = requests.get(URL)
soup = BeautifulSoup(page.text)
# print(soup.prettify())

author = soup.find("p", class_ = "author")
print(author.text.strip("by "))

title = soup.find("h1", class_ = "title is-2")
print(title.text)

recipe = soup.find("div", class_ = "md")
print(recipe.text) """



# response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
# film_data = response.json()

# film_list = film_data['data']['films']

# longest_film_length = 0
# longest_film = None

# for item in film_list:
#     if int(item['running_time']) > int(longest_film_length):
#         longest_film_length = item['running_time']
#         longest_film = item

# print(f"The longest film is {longest_film_length} minutes long.")
# print(f"The longest films title is : {longest_film['title']}")

# for item in film_list:
#     if int(item["running_time"]) == int(longest_film_length):
#         print(item['release_date'], item["original_title"])






""" # Get data from API and dump it into a new file named films.json
import json
import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
data = response.json()

with open("films.json", "w") as fout:
    json.dump(data, fout) """

""" import json

with open("films.json", "r") as fin:
    data = json.load(fin)

print(len(data))  # OUTPUT: 21
print(type(data)) """






""" import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)

soup = BeautifulSoup(page.text)
# Converting for loop into list comprehension
import time

# for loop
start = time.time()
links = soup.find_all("a")
parsed_links = []
for link in links:
    parsed_links.append(link["href"])
end = time.time()
print(end - start)

# List Comprehension
start = time.time()
links = [link["href"] for link in soup.find_all("a")]
end = time.time()
print(end-start) """

import random 

num_list = [1,2,3,4,5,6,7,8,9]
selected_nums = []
max_num = 6

while len(selected_nums) < max_num:
    num = random.choice(num_list)
    selected_nums.append(num)
    num_list.remove(num)

print(selected_nums)