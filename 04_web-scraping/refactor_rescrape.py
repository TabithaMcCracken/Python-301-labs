# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

URL = "https://www.14ers.com/14ers"
html_file = 'scraped_content.html'
peaks_list = []

def get_page_content(URL):
    """Gets response from a HTTP call to the URL."""
    page = requests.get(URL)
    return page

def save_page_to_local_html_file(html_content):
    """Save the response to a local html file."""

    with open ('scraped_content.html', 'w') as file:
        file.write(html_content)
        print('The content has been saved to "scraped_content.html"')





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
        # cols = row.find_all('td')
        # cols = [
        #     col.find('div', attrs={'class' : 'hide-8'}).text.strip() if col.find('div', attrs={'class' : 'hide-8'}) else col.text.strip()
        #     for col 
        #     in cols
        # ]

        cols = []
        for col in row.find_all('td'):
            hide8 = col.find('div', attrs={'class' : 'hide-8'})
            if hide8:            
                cols.append(hide8.text.strip())
            else:
                cols.append(col.text.strip())
            
        # print(cols)
        peak_data.append(cols)



    return peak_data


if __name__ == "__main__":
    # scrape_website(URL)
    html_content = get_page_content(URL)
    if html_content.status_code == 200:
        page_content = html_content.text
        print("Scraping Successful.")
    else:   
        print("Error: Failed to retrieve the web page.")

    # Convert to text 
    html_text = html_content.text

    # Save to local file
    save_page_to_local_html_file(html_text)
    
    # Get the peaks list
    peaks_list = parse_file(html_file)
    print("Here is all the basic peak info: ")
    for peak in peaks_list:
        print(peak)