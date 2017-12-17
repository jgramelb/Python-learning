#write a program to read through a mail log,
#build a histogram using a dictionary to count how many messages
#have come from each email address, and print the dictionary


fname = input('Enter a file name: ')
try:
    fhandle = open(fname)

except:
    print('File cannot be read', fname)
    exit()


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


print(countdct)
