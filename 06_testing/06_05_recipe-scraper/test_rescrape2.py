
import pytest
import rescrape

class TestRescrape:
    BASE_URL = "https://codingnomads.github.io/recipes/" # Index page
    url = f"{BASE_URL}recipes/11-making-my-own-baguet.html" # A recipe page

    # requests can establish a connection and receive a valid response
    def test_get_page_content(self):
        # Check index page
        index_page = rescrape.get_page_content(self.BASE_URL)
        assert index_page.status_code == 200
        # Check recipe page
        page = rescrape.get_page_content(self.url)
        assert page.status_code == 200

    # response contains html
    def test_get_html_content_returns_html_string(self):
        # Check index page
        index_page = rescrape.get_html_content(self.BASE_URL)
        assert "<!DOCTYPE html>" == index_page[0:15]
        # Check recipe page
        page = rescrape.get_html_content(self.url)
        assert "<!DOCTYPE html>" == page[0:15]


    # Converts an HTML string to a BeautifulSoup object
    def test_convert_html_to_beautifulsoup_object(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        assert str(type(soup)) == "<class 'bs4.BeautifulSoup'>"

    # Can get links from the index page
    def test_get_recipe_links_gets_links(self):
        index_html = rescrape.get_html_content(self.BASE_URL)
        index_soup = rescrape.make_soup(index_html)
        result = rescrape.get_recipe_links(index_soup)
        assert len(result) > 0

    # Can identify the author of a recipe
    def test_get_author_gets_aurthor(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        author = rescrape.get_author(soup)
        assert len(author) > 0
        assert "Jadafaa" == author

    # Can get the main recipe text
    def test_get_recipe_gets_recipe(self):
        html = rescrape.get_html_content(self.url)
        soup = rescrape.make_soup(html)
        recipe = rescrape.get_recipe(soup)
        assert len(recipe) >= 0
        assert type(recipe) == str
