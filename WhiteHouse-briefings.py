# Import Libraries

import requests
from bs4 import BeautifulSoup

# Store webpage to be accessed in variable
result = requests.get("https://www.whitehouse.gov/briefings-statements/")

# Store content from that webpage
src = result.content

# Process content with BeautifulSoup module
soup = BeautifulSoup(src, 'lxml')

# Create list to store links we find
urls = []

# All links on this page are under an "h2" HTML heading
for h2_tag in soup.find_all("h2"):  # find h2 tags (all h2 headings)
    a_tag = h2_tag.find('a') # find 'a' tag inside h2 tag (actual link)
    urls.append(a_tag.attrs["href"]) # add link to urls list starting with "href" tag

# Make sure list is populated
print(urls)
