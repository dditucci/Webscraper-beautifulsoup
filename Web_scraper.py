# Import Libraries

import requests
from bs4 import BeautifulSoup

# Create variable for webpage to be accessed (Google)
result = requests.get("https://www.google.com/")

# Make sure website is being accessed (200 = good, 404 = bad)
print(result.status_code)

# Check HTTP header to make sure the correct page is being accessed
print(result.headers)

# Extract content from page and store in variable
src = result.content

# Create soup object by passing src variable into BeautifulSoup class
# This will process the source material to be used with BeautifulSoup module
soup = BeautifulSoup(src, 'lxml')

# Find all links on the page by finding HTML "a" tags
links = soup.find_all('a')
print(links)

# Extract certain desired links (Links with word "About" in this example)
# Loop through all links in var "links"
for link in links:
    if "About" in link.text:  # See if "About" is in the text
        print(link)           # Print link if it contains "About"
        print(link.attrs["href"]) # Print href attribute for link with "About"
    
