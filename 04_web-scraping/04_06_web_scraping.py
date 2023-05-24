# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.



import requests
from bs4 import BeautifulSoup

URL = "https://www.14ers.com/14ers"

# # Scrape the website and save the response to a local html file
# # Send a GET request to the URL
# response = requests.get(URL)

# # Check if the request was successful
# if response.status_code == 200:
#     # Get the HTML content
#     html_content = response.text

#     # Save the extracted content into a text file
#     with open ('scraped_content.html', 'w') as file:
#         file.write(html_content)

#     print('Scraping successful. The content has been saved to "scraped_content.html"')
# else:
#     print('Error: Failed to retrieve the web page')


# Option 2: Get html from website
# Make a GET request to fetch the raw HTML content
# response = requests.get(URL)
# soup = BeautifulSoup(response.content, 'html.parser')


# Read the HTML file
with open("scraped_content.html", "r", encoding="utf-8") as file:
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
 
# Print the first column
for item in peak_data:
    print(item[0])
