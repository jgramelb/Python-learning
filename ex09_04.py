#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.

fname = input("Enter file name:")
try:
    fhandle = open(fname)
except:
    print('Please enter a valid file name. ''You typed:',fname)
    quit()


countdct = dict()

for line in fhandle:
    #print line

    line = line.rstrip()
    #look for line that start with "From:"
    if not line.startswith('From:'):
        continue
	#create words
    words = line.split()
    words = words[1:2]
    for word in words:
        if word not in countdct:
            countdct[word] = 1
        else:
            countdct[word] = countdct[word] + 1


#print(countdct)


#create a list of the values of countdct
lst = list(countdct.values())
#sort it out (optional)
lst.sort()

#find the MAX value
largest = None
for value in lst:
    if value is None or value:
        largest = value
    elif value > largest:
        largest = value

#for key in the list
for key in countdct:
    #if the value of the key is the largest value
    if countdct[key] == largest:
        #print its value to the right of the key
        print(key, countdct[key])
