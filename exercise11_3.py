#shortened version of 11_2, using sample data 11_2.txt


import re
print(sum([int(x) for x in re.findall('[0-9]+', open('sampledata11_2.txt').read())]))
