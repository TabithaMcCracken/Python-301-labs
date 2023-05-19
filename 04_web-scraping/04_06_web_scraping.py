# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.



import requests
from bs4 import BeautifulSoup

URL = "https://www.14ers.com/14ers"

# # Scrape the website and save the response to a local file
# # Send a GET request to the URL
# response = requests.get(URL)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Extract the desired information from the parsed HTML
#     # Replace this with your specific logic to extract the content you need
#     extracted_content = soup.get_text()

#     # Save the extracted content into a text file
#     with open('scraped_content.html', 'w') as file:
#         file.write(extracted_content)

#     print('Scraping successful. The content has been saved to "scraped_content.txt"')
# else:
#     print('Error: Failed to retrieve the web page')



# Make a GET request to fetch the raw HTML content
html_content = requests.get(URL).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")
print(soup.title.text) # print the parsed data of html
# Parse content of file
peaks_table = soup.find('table', attrs={'class' : 'v3-table rowhover alternaterowcolors1'})
peaks_table_data = peaks_table.tbody.find_all('tr')

headings = []
for td in peaks_table_data.find_all("td"):
    headings.append(td.b.text.replace('\n', ' ').strip())

print(headings)

# with open ('scraped_content.html', 'r') as file:
#     file_content = file.read()
#     soup = BeautifulSoup(file_content, 'html.parser')

# print(type(soup))
# print(soup.find('meta')) # returns None
# for link in soup.find_all('a'):
#     print(link.get('href'))
# x = soup.body.find_all('div', attrs={'class':'container'}).text