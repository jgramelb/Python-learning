#ex6-3

#Exercise 3:Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter):
    n = 0
    for string in word:
        if string == letter:
            n = n + 1

    print(n)

count('banana','a')
