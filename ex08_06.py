#ex8.6

empty = []
while True:
    #Asks user for number
    num = input('Enter a number: ')
    #if they type done, they are pau with code
    if num == 'done' :
        if empty == []:
            print('Please enter a number!')
        break
        print('Enter a number:',num)
	#try except:
    try:
        num = int(num)
    except:
        continue
	#print input with the number
    print('Enter a number:', num)
    #append the number to the empty list
    empty.append(num)

#calculate min and max
minofempty = min(empty)
maxofempty = max(empty)

#convert min and max to float
fminofempty=float(minofempty)
fmaxofempty=float(maxofempty)

#Print max
print('Maximum:', fmaxofempty)
#Print min
print('Minimum:', fminofempty)
