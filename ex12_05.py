#Exercise 1 from book for chapter 12
#call it 12_05.py

#change socket program so that is counts the number of characters it has recieved
#and stops displaying any text after it has shown 3000 characters.
#The program should retrieve the entire document and count the total number of characters
    #and display the count of number of characters at the end of the document


import socket

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

    elif HOST.startswith('https://'):
        #use split to break the URL so that I can extrac the host name for socket connect call.
        HOSTname = HOST.split('/')
        HOSTname = HOSTname[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #reads webpage here.
        mysock.connect((HOSTname, 80))

    elif not HOST.startswith('http'):
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


#initialize counts for data
counts = 0

#We want to also read the headers!
while True:
    #This is where we try to receive the data
    data = mysock.recv(512) #512 represents how many characters we get each time we ask for new data
    data = data.decode().strip()
    counts = counts + len(data) #how many characters in each call for data is characterized by len(data)
    #if there is no data, break out
    if (len(data) < 1):
        break
    #we want to print out headers and file data up to 3000 characters
    if counts < 3000:
        print(data)

#print the counts
print('There are',counts, 'characters')
mysock.close()
#close the socket, stop reading from webpage~
