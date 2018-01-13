#Exercise 3 out of chapter 12
#12.6

#Instructions:
#Use urllib to replicate the previous exercise of (1) retrieving the document from
    #a URL, (2) displaying up to 3000 characters, and (3) counting the overall
    #number of characters in the document. Don't worry about the headers for
    #this exercise, simply show the first 3000 characters of the document contents.

import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

try:
    HOST = input('Enter a URL - ') #prompts user for the URL for that it can read any webpage
    HOST = HOST.lower() #convert the input into lowercase letters

except:
    print('You have entered an improperly formatted or non-exisent URL - ', HOST)
    exit()

fhand = urllib.request.urlopen(HOST)

#initialize the counts
counts = 0
#Let's read the first 3000 characters.
#here, we read each line in the file
for line in fhand:
    #We strip it of whitespaces on the right and left of each line.
    line = line.decode().strip()
    #Here is the formula for how many characters there are in a line. We sum it up here
    counts = counts + len(line) #length of line gets you how much characters there are in a line
    #We want to print out the document up to 3000 characters here
    if counts < 3000:
        print(line)

#Print out how many characters in the document
print('There are',counts, 'characters')
