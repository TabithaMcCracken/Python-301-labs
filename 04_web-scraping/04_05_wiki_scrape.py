# Done
# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

URL = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup
import re
import random

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

# Filter navigation links
filtered_links = []
for link in links:
    if 'nav' not in link.get('class', []) and 'menu' not in link.get('class', []) and 'footer' not in link.get('class', []):
        filtered_links.append(link.get('href'))

# Create a list of the full links (start with http)
page_links = []

#Rewritten as a list comprehension
page_links = [item for item in filtered_links if item[0:4] == "http"]
print("Here are the page links that start with 'http':")
for item in page_links:
     print(item)

# Create list of links that are wiki links (start with "/wiki")
wiki_page_links = [item for item in filtered_links if item[0:5] == "/wiki"]

# Create list of wiki links excluding 'Category', 'Wikipedia', and 'Help" links
parsed_wiki_page_links = []
for item in wiki_page_links:
    if item[0:14] != "/wiki/Category" and item[0:15] != "/wiki/Wikipedia" and item[0:10] != "/wiki/Help":
        parsed_wiki_page_links.append(item)



# Prepend link info to make links valid url's
prepended_wiki_links = []
for item in parsed_wiki_page_links:
    prepended_wiki_links.append("https://en.wikipedia.org" + item)

print("Here are the internal wiki page links:")
for item in prepended_wiki_links:
    print(item)


# Gets a random link from the list
link_list_length = len(prepended_wiki_links)
print(link_list_length)

random_link = random.choice(prepended_wiki_links)
print(f"Here is a random link from the website: {random_link}")


# Gets html from the random_link and writes it to a file
response2 = requests.get(random_link)
html_content = response2.text

soup2 = BeautifulSoup(html_content, "html.parser")
content = soup2.get_text()

with open ("webpage.txt", "w", encoding="utf-8") as file:
    file.write(content)
