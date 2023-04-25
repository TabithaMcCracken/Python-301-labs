# import requests
# import time
# from bs4 import BeautifulSoup

# BASE_URL = "https://codingnomads.github.io/recipes/"
# page = requests.get(BASE_URL)

# soup = BeautifulSoup(page.text)
# # Converting for loop into list comprehension

# # For Loop
# start = time.time()
# links = soup.find_all("a")
# parsed_links = []
# for link in links:
#     parsed_links.append(link["href"])
# end = time.time()
# print(end - start)

# # List Comprehension
# start = time.time()
# links = [link["href"] for link in soup.find_all("a")]
# end = time.time()
# print(end-start)

# # For Loop
# links = soup.find_all("a")
# parsed_links = []
# for link in links:
#     parsed_links.append(link["href"])

# # List Comprehension
# links = [link["href"] for link in soup.find_all("a")]


