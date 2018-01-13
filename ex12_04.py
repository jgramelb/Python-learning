#Exercise 1 from book for chapter 12
#call it 12_04.py
#Exercise 1: Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL into its
# component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user
# enters an improperly formatted or non-existent URL.

import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

try:
    HOST = input('Enter a URL - ') #prompts user for the URL for that it can read any webpage
    HOST = HOST.lower()

    #convert the input into lowercase letters

    #if it line starts with https://:

    if HOST.startswith('http://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))
    elif HOST.startswith('https://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))

    elif not HOST.startswith('https://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
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
soup = BeautifulSoup(HOSTname, 'html.parser')
#want to write loop that receives data in _ chunks from the socket
while True:
    #This is where we try to receive the data
    data = mysock.recv(512) #512 represents how many characters we get each time we ask for new data
    if (len(data) < 1):
        break
#You want to read the webpage aka the data
#&&& you want to print the data until there is no more data to read!
    print(data.decode())

#whern there is no more data... close it!
mysock.close()
