#ex8.1
#Prompt user what string wanted to put in here
s = input('Enter string here:')
#Convert the string into a list
t = list(s)

#Create function the removes the first and last element of list- call it chop
def chop(t):
	#If the string is of length two or less, return none
    if len(t) <= 2:
        return None
    #If the string is of length 3 or more:
    else:
        #Find its last index
        endpos = len(t)-1
        #and return from index 1 (which is after the first letter) to its end position
        return t[1:endpos]

#Forgot? What did we input for s
print('I entered string:', s)
#And I recieved the list
print('I got the list',t)

#Print the function with list
print(chop(t))
