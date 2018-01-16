#write program similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, 
  #read the XML data from that URL using urllib and 
  #then parse and extract the comment counts from the XML data
  # compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_45239.xml (Sum ends with 18)


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = input('Enter a URL')
#'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
