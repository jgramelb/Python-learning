import re

fname = input('Enter a file name: ')
fhandle = open(fname)

#initialize count for 0
count = 0
#want to create a list to add all numbers to
lst = list()
#want to read file here
for line in fhandle:

    #strip the line of stupid spaces
    line = line.rstrip()
    #make t all lowercase
    line = line.lower()
    #print for reference
    #print(line)

    #look for all integers using re.findall()
    x = re.findall('^New .*: ([0-9]+)',line)
    #look for regular expressin of 0-9 +  to convert strings to integers
    if len(x) > 0 :

        #for each number, add to the empty list. keep extending.
        lst.extend(x)

    count = count + 1
#reference: print this list of all numbers(in string form) in the thing
#print(lst)

#initialize the taol
total = 0
#for each number inside of the list, add them up
for num in lst:
    #want to convert number string into integers
    numint = int(num)
    #add to total
    total = total + numint
#print out final total/count
print(total/count)
