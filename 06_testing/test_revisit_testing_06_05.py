import unittest
import validators
import requests
import revisit_testing_06_05
from bs4 import BeautifulSoup

class TestRevisit_testing_06_05 (unittest.TestCase):

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
        self.assertEqual(revisit_testing_06_05.get_page_content(BASE_URL).status_code, 200)

    # the HTML can be successfully converted to json dict
    def test_response_converted_to_json(self):
        BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
        response = revisit_testing_06_05.get_page_content(BASE_URL)
        self.assertEqual(type(revisit_testing_06_05.convert_to_json(response)), dict)

    # URL's extracted can establish a connection and receive a valid response
    def test_valid_urls(self):
        BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
        response = revisit_testing_06_05.get_page_content(BASE_URL)
        pokemon_data = response.json()
        pokemon_urls = revisit_testing_06_05.create_list_of_pokemon_urls(pokemon_data)
        sc_for_poke_urls = [True for url in pokemon_urls if requests.get(url).status_code == 200]
        self.assertEqual(all(sc_for_poke_urls), True)

    # do I need to do these tests?
    # can identify the id

    # can identify the name

    # can identify the type

if __name__ == "__main__":
    unittest.main()