#Exercise 1 from the book

#Change either the www.py4e.com/code3/geojson.py or www.py4e.com/code3/geoxml.py
    #to print out the two-character country code from the retrieved data.
    #Add error checking so your program does not traceback if the country
    #code is not there. Once you have it working, search for "Atlantic Ocean"
    #and make sure it can handle locations that are not in any country.

import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve Address Given ====')
        print('*   ',address, 'is not located in any country')
        #print(data)
        continue


    #print(json.dumps(js, indent=4))
    #for reference:
    #print(data)

    results = js["results"][0]["address_components"]
    for i in results:
        if i["types"] == ['country', 'political']:
            twocharactercountrycode = i["short_name"]
            print('Two Character Country Code - ', twocharactercountrycode)

    break
