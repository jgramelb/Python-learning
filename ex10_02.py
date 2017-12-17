#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()

    #if line does not start with "From ", continue
    if not line.startswith('From '): continue
    #if it does, split it into words
    words = line.split()

    #for the time in the words, i want to split it into hours
    for time in words[5:6]:
        hour = time[0:2]
        #histogram of hours
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1

#Create a list
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))
lst.sort()
#print(lst)

for key, val in lst:
    print(key,val)
