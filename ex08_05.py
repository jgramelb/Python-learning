#ex8.5
#     8.5 Open the file mbox-short.txt and read it line by line.
#     When you find a line that starts with 'From '
#     like the following line:
#  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#     You will parse the From line using split() and
#     print out the second word in the line
#     (i.e. the entire address of the person who sent the message).
#     Then print out a count at the end.

fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('Please enter correct file name. You entered:', fname)
    quit()

count = 0
#read txt file line by line
for line in fhandle:
    #print(line)

#When you find a line that starts with 'From '
	if not line.startswith('From '): continue
#Split the line into words
	words = line.split()

#print out the second word in the line
	#print(words[1])
	count = count + 1

#print count
print("There were",count, "lines that starts with 'From '")
