# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

# BASE_URL = "https://ghibliapi.herokuapp.com/"
import requests
import json


# BASE_URL = "https://ghibliapi-iansedano.vercel.app"
BASE_URL = "https://ghibliapi-iansedano.vercel.app/api/species"

response = requests.get(BASE_URL)
film_data = response.json()
# print(film_data)

film_list = film_data['data']['species']
print(film_list)

for item in film_list:
    if item['name'] == 'Cat':
        print(item['name'])

# species_list = response['data']['species']
# print(species_list)






# response.raise_for_status()
# print(response.status_code)





