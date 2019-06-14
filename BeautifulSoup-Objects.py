# Import Library

from bs4 import BeautifulSoup

# Create basic/fake HTML site to use for this exercise
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

# Save file ("publish" webpage) 
with open('index.html', 'w') as f:
    f.write(html_doc)

# Create BeautifulSoup object
soup = BeautifulSoup(html_doc, 'lxml')

# Use prettify to print content in formatted HTML
print(soup.prettify())

# Find 1st occurence of bold content with HTML tags 'b'
print(soup.b)

# Alt way to find 1st occurence of bold content with HTML tags 'b'
print(soup.find('b'))

# Find 1st occurence of paragraph content with HTML tags 'p'
print(soup.p)

# Find all occurences of bold content with HTML tags 'b'
print(soup.find_all('b'))

# Find name of 1st bold tag 'b'
print(soup.b.name)

# Alter the name of 1st 'b' tag
tag = soup.b   # Create object
print(tag)

tag.name = "blockquote"  # Change name
print(tag)

# Find specific bold tag
tag = soup.find_all('b')[1]
print(tag)

# Access and print id tag
print(tag['id'])

# Access another tag
tag  =soup.find_all('b')[2]
print(tag)

# Access and print tag id like above
print(tag['id'])

# Access and print other attribute
print(tag['another-attribute'])

# Print tag
print(tag)

# Print all attributes of specific tag
print(tag.attrs)

# Change values of attributes
print(tag)
tag['another-attribute'] = 2 # Change value of 'another-attribute'
print(tag)

# Delete an attribute from a tag
print(tag)
del tag['id'] # Delete 'id' attribute
print(tag)

# Delete another attribute from a tag
print(tag)
del tag['another-attribute'] # Delete 'another-attribute' attribute
print(tag)

# Define tag to work with
tag = soup.find_all('b')[2]
print(tag) # Print entire tag
print(tag.string) # Print only the content between tags

# Alter the string content between tags
tag.string.replace_with("This is another string")  # Replace content with new string
print(tag)


