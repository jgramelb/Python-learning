#ex8.4
#   8.4 Open the file romeo.txt and read it line by line.
#   For each line, split the line into a list of words using the
#   split() method. The program should build a list of words.
#   For each word on each line check to see if the word is already
#   in the list and if not append it to the list.
#   When the program completes, sort and print the resulting words
#   in alphabetical order.


fname = input('Enter file name')
try:
    fhandle = open(fname)
except:
    print('Please enter file name.\n You typed:', fname)
    quit()


empty = []

#read txt file line by line
for line in fhandle:
    #print(line)

#split the line into words
	line = line.split()

#for each word on the line
	for words in line:

#check to see if the word is already in the list

		if words in empty:
			continue
#otherwise in emptylist, append the words to empty list
		empty.append(words)
#sort
empty.sort()
#print
print(empty)
