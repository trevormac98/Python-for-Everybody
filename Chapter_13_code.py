'''Scraping numbers from HTML using Beautiful Soup. In this assignment you will write a Python program similar to... The program will use
urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
Actual Data: http://py4e-data.dr-chuck.net/comments_125026.html (sum ends with 53)

You do not need to save these files to your folder since your program will read the data directly from the URL. 

The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
YOu need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete
the assignment. '''

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
# Look at the parts of a tag

    #print tag.contents[0]
    num = float(tag.contents[0])
    #print num
    sum = sum + num
    count = count + 1

print ('count:', count)  
print ('sum:', sum)  