#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_45962.html (Sum ends with 32)


#work from samplecode
from urllib.request import urlopen
from bs4 import BeautifulSoup

#Ask user to enter URL
url = input('Enter - ')
#read the html page
html = urlopen(url).read()

#beautiful soup parser built into python
soup = BeautifulSoup(html, "html.parser")

#initalize total to be 0
total = 0
# Retrieve all of the SPAN anchor tags
tags = soup('span')

#for each span tag
for tag in tags:

    #get each tag class="comments"
    #print('URL:', tag.get('class="comments"', None))
    #just get the contents of the tag
    num = tag.contents[0]
    #convert the string of numbers into actual numbers
    num = int(num)
    #now add up the total
    total = total + num
#print out the total
print(total)
