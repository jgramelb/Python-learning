#12.7

#Exercise 4 from book
#Instructions:
#Change the urllinks.py program to extract and count paragraph (p) tags from the
    #retrieved HTML document and display the count of the paragraphs as the
    #output of your program. Do not display the paragraph text, only count them.
    #Test your program on several small web pages as well as some larger web pages.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

try:
    HOST = input('Enter a URL - ') #prompts user for the URL for that it can read any webpage
    HOST = HOST.lower() #convert the input into lowercase letters

except:
    print('You have entered an improperly formatted or non-exisent URL - ', HOST)
    exit()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open up the URL file
fhand = urllib.request.urlopen(HOST, context=ctx)
#Parse it with BeautifulSoup, but we don't want to show it.
soup = BeautifulSoup(fhand, 'html.parser')

#here, we read each line in the file // BUT WE DONT NEED IT IN THIS EXAMPLE.
# WE ARE NOT TRYING TO READ THE HTML!!!!
#for line in fhand:
    #We strip it of whitespaces on the right and left of each line.
    #line = line.decode().strip()
    #just simply print out the URL file
    #print(line)

#initialize the counts
paragraphcounts = 0
# Retrieve all of the paragraph tags
tags = soup('p')
for tag in tags:
    #get the tag. call it ptag
    ptag = tag.get(None)
    #count how many <p> you see.
    paragraphcounts = paragraphcounts + 1

#print the counts
print('There are',paragraphcounts,'<p> tags!')
