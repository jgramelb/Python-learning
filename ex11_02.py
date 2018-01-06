#assignment 11 exercise 2

import re

fname = input('Enter a file name: ')
fhandle = open(fname)

#want to read file here

total = 0
count = 0
for line in fhandle:
    #strip the line of stupid spaces
    line = line.rstrip()
    #print for reference
    #print(line)

    #look for all integers using re.findall() with pattern of New Revision
    x = re.findall('New Revision: ([0-9.]+)',line)

    #for each item in the string, we will iterate over each character
    for nums in range(len(x)):
                            #if it is a string number, convert to string
                            #ADD IT TO TOTAL :)
        total = total + int(x[nums])
        count = count + 1
#reference: print this list of all numbers(in string form) in the thing
average = total/count
print(average)

