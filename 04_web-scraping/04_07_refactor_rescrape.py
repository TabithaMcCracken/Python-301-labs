# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

URL = "https://www.14ers.com/14ers"
html_file = 'scraped_content.html'
peaks_list = []

def scrape_website(URL):
    """Scrape a website and save the response to a local html file

    Args:
        URL (str): URL for website to scrape
    """
    # Send a GET request to the URL
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text

        # Save the extracted content into a text file
        with open ('scraped_content.html', 'w') as file:
            file.write(html_content)

        print('Scraping successful. The content has been saved to "scraped_content.html"')
    else:
        print('Error: Failed to retrieve the web page')


def parse_file(html_file):
    """Parse the file for the first column of data from the table

    Args:
        html_file (html file): file to be parsed

    Returns:
        list: items from the table
    """

    # Read the HTML file
    with open(html_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    peak_data = []
    # Parse content of file
    # Get the right table
    peaks_table = soup.find('table', attrs={'class' : 'v3-table rowhover alternaterowcolors1'})
    # Find the body of the table
    table_body = peaks_table.find('tbody')
    # Get the rows
    rows = table_body.find_all('tr')
    # Get the columns
    for row in rows:
        cols = row.find_all('td')
        cols = [ ele.text.strip() for ele in cols]
        peak_data.append([ele for ele in cols if ele])

    return peak_data


if __name__ == "__main__":
    # scrape_website(URL)

    peaks_list = parse_file(html_file)

    for peak in peaks_list:
        print(peak[0])