#ex9.1
#Write a program that reads the words in words.txt & stores them as keys in the dictionary. It doesn't matter what the values are.
#Check to see if the string is in the dicitonary
fname = input("Please enter file name: ")
fhandle = open(fname)


#initialize or create empty dictionary
dct = dict()

#for the line in fhandle
for line in fhandle:
    words = line.split()
    #for the word is in words
    for word in words:
        #if the word is in the words lsit
        if word in words:
            #add it
            dct[word] = 1
        #else:
            #otherwise, just add a  value?
            #dct[word] = dct[word]+1
#print new dictionary
print(dct)

#Check to see if a word is in the dictionary
key = input("Enter a word to look up")

if key not in dct:
    print('False')
else:
    print('True')
