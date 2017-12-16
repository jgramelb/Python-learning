#Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo". The program should behave normally for all other files which exist and don't exist. Here is a sample execution of the program:

fname = input('Enter file name:')

try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    else:
        print('Error, please type the file name correctly:', fname)
    exit()

#print(fhand)

#initialize total and count to be 0
total = 0
count = 0

#for every line in file, print it out
for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    #isolate the numbers
    pos = line.find(':')
    #print(pos)
    npos = line[pos+1:]
    #print(npos)
    #Isolate the numbers to be float numbers
    fpiece = float(npos)
    #print(fpiece)
    #print(line)
    total = total + fpiece
    count = count + 1
print('Average spam confidence:', total/count)
