import unittest
import requests
import revisit_testing_06_05
from bs4 import BeautifulSoup

class TestRevisit_testing_06_06 (unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "https://pokeapi.co/api/v2/pokemon/?limit=6&offset=0"
        self.individual_poke_result = revisit_testing_06_05.get_individual_pokemon_results_data(self.BASE_URL)[3]

    # requests can establish a connection and receive a valid response
    def test_get_valid_html_response(self):
        index_page = revisit_testing_06_05.get_page_content(self.BASE_URL)
        self.assertEqual(index_page.status_code, 200)

    # the HTML can be successfully converted to json dict
    def test_response_converted_to_json(self):
        index_json = revisit_testing_06_05.convert_to_json(self.BASE_URL)
        self.assertEqual(type(index_json), dict)

    # URL's extracted can establish a connection and receive a valid response
    def test_valid_urls(self):
        pokemon_urls = revisit_testing_06_05.create_list_of_pokemon_urls(self.BASE_URL)
        sc_for_poke_urls = [True for url in pokemon_urls if revisit_testing_06_05.get_page_content(url).status_code == 200]
        self.assertEqual(all(sc_for_poke_urls), True)

    # Check that pokemon list is a list
    def test_individual_poke_is_list(self):
        individual_poke_results = revisit_testing_06_05.get_individual_pokemon_results_data(self.BASE_URL)
        self.assertEqual(type(individual_poke_results), list)

    # can identify the id
    def test_id_is_int(self):
        result = revisit_testing_06_05.get_poke_id(self.individual_poke_result)
        self.assertEqual(type(result), int)

    # can identify the name
    def test_name_is_str(self):
        result = revisit_testing_06_05.get_poke_name(self.individual_poke_result)
        self.assertEqual(type(result), str)

    # can identify the type
    def test_type_is_list(self):
        result = revisit_testing_06_05.get_poke_types(self.individual_poke_result)
        self.assertEqual(type(result), list)


if __name__ == "__main__":
    unittest.main()