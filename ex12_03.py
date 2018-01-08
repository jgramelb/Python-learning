#following links in python
#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Graham.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: A

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#create a list to store your URL data
lstsites = list()

#enter starting URL here
url = input('Enter URL: ')

#enter how many times you want to do this
count = input('Enter count: ')
count = int(count)
#enter which position to follow the link at
position = input('Enter position: ')
position = int(position)

#we will iterate over count times
for i in range(count):
    #print that we are retrieving some sort of URL
    print('Retrieving:', url)
    #query the website and return the html
    html = urllib.request.urlopen(url).read()
    #parse the content of the request with beautifulsoup
    soup = BeautifulSoup(html, 'html.parser')
    #look for the <a> anchor tags
    tags = soup('a')
    for tag in tags:
        #site = tag.get('href', None).split()
        #append it to your list containing all of the sites
        lstsites.append(tag)
    #find the URL in the nth position
    url = lstsites[position-1].get('href', None)
    #reference:
    #print(lstsites[position-1])

    #DELETE THE LIST SO THIS  DONT BLOW UP
    del lstsites[:]
#print the last URL homie
print('Retrieving:', url)
