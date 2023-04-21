# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

import requests
response = requests.get("https://codingnomads.co/")
print(response.text)



response.raise_for_status()
print(response.status_code) # Status is 200, so not an issue with that
print(response.headers["content-type"])

# Check type 
# if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json"):
#     try:
#         print.response.json()
#     except ValueError:
#         print("This is not a 204")

