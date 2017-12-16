#7.2

#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
fh = open(fname)
for line in fh:
    #for every line, take out the whitespace
    line = line.rstrip()
    #if the line doesn't have X-DSPAM...., continue
    if not line.startswith("X-DSPAM-Confidence:") : continue
	#we start isolating the pieces
    pos = line.find(':')
    ##cont. print(pos)
    newpos = line[pos+1:]
    ##continued print(newpos)
    fpos = float(newpos)
    #print(fpos)
    #print(line)
    #***total it up
    total = fpos + total
    #count it up
    count = count + 1

    #print(count)

print('Average spam confidence:', total/count)
