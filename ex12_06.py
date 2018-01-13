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

    if HOST.startswith('http://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))
        fhand = urllib.request.urlopen(HOST)

    elif HOST.startswith('https://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))

    elif not HOST.startswith('https://'):
        #use split to break the URL so that I can extract the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[0]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))
except:
    print('You have entered an improperly formatted or non-exisent URL - ', HOST)
    exit()

#get command
cmd = ('GET '+ HOST + ' HTTP/1.0\r\n\r\n').encode() #\r\n\r\n is the default windows style for line separator
#send information from website to me.
mysock.send(cmd)
fhand = urllib.request.urlopen(HOST)

#No need write out the headers.
#let's control how much data we can read at one time, every time we ask for new data.
while True:
    #REceive data here
    data = mysock.recv(512) #512 represents how many characters we get each time we ask for new data
    #If there is no data,  break
    if (len(data) < 1):
        break
#No need print the data

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
#done reading from the socket/ done reading from webpage.
mysock.close()
