import unittest
import requests
from bs4 import BeautifulSoup
import refactor_rescrape

class TestRescrape(unittest.TestCase):

    def test_get_valid_html_response(self):
        BASE_URL = "https://www.14ers.com/14ers"
        index_page = refactor_rescrape.get_page_content(BASE_URL)
        self.assertEqual(index_page.status_code, 200)
    pass
    # requests can establish a connection and receive a valid response

    # the response contains HTML code

    # the HTML can be successfully converted to a Beautiful Soup object

    # can identify all links from the index page

    # can identify the author of a recipe

    # can get the main recipe text

if __name__ == "__main__":
    unittest.main()


