#write program similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, 
  #read the XML data from that URL using urllib and 
  #then parse and extract the comment counts from the XML data
  # compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_45239.xml (Sum ends with 18)


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
URL = input('Enter URL with XML file - ')
print('Retrieving', URL)

#REtrive data here
uh = urllib.request.urlopen(URL)
data = uh.read()

#Print how many characters we've retrieved in the whole xml document
print('Retrieved', len(data), 'characters')

#We get data from XML, call it tree
tree = ET.fromstring(data)

#We make a list of all of the count tags
counts = tree.findall('comments/comment/count')
#We print how many XML elements
print('Count', len(counts))

#initialize total
total = 0
#want to sum up all of the count in here
for count in counts:
    #print(count.text)
    count = int(count.text)
    total = total + count

print('Sum:', total)
