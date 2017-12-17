#Write a program that categorizes each mail message by which day of the week the commit was done

fname = input('Enter a file name: ')
try:
    fhandle = open(fname)

except:
    print('File cannot be read', fname)
    exit()

#look through lines in fhand


countdct = dict()

for line in fhandle:
    #print line
    line = line.rstrip()
    #look for line that start with "From"
    if not line.startswith('From'):
        continue
	#create words
    words = line.split()
    words = words[2:3]
    for word in words:
        if word not in countdct:
            countdct[word] = 1
        else:
            countdct[word] += 1


print(countdct)
