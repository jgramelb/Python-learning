#ex13_02.py

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a #URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of #the numbers in the file and enter the sum below:

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_45240.json (Sum ends with 9)


import json
import urllib.request, urllib.parse, urllib.error


address = input('Enter location - ')


while True:
    #print('')
    #address = input('Enter location - ')
    #if len(address) < 1: break

    url = address #+ urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()#.decode()
    print('Retrieved', len(data), 'characters')
    #print(data)
    break

jsinfo = json.loads(data)

commentcount = jsinfo['comments']#[0]['count']
#We print how many comments count elements
print('Count', len(commentcount))

#initialize total
total = 0
#want to sum up all of the count in here
for count in commentcount:
    #print('Count:', count['count'])
    count = int(count['count'])
    total = total + count

print('Sum:', total)
