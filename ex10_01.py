#ex10.1

#ex 10.1

fname = input("Enter a file name:")
try:
    fhandle = open(fname)

except:
    print('Please enter a valid file name. You typed:',fname)
    quit()

#initialize dictionary
countdct = dict()
for line in fhandle:
    line = line.rstrip()
    #look for line that starts with "From"
    if not line.startswith('From '):
        continue
    words = line.split()
    words = words[1:2]
    for word in words:
        if word not in countdct:
            countdct[word]=1
        else:
            countdct[word] = countdct[word]+1
print(countdct)

#create a list of the values of countdct

lst=list(countdct.values())
lst.sort()

#find max value
largest = None
for value in lst:
    if value is None or value:
        largest = value
    elif value > largest:
        largest = value

#for key in the list, find largest key and print:
for key in countdct:
    #if the value of the key is the largest value,
    if countdct[key] == largest:
        #print
        print(key, countdct[key])
