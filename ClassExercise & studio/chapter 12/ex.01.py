'''Write a program that allows the user to enter a string.
 It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with
 the number of times each letter occurs. Case should be ignored. A sample run of the program might look this this:

Please enter a sentence: ThiS is String with Upper and lower case Letters.
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$

'''

x = input("Enter a sentence")

x = x.lower()   # convert to all lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in x:
        if char in alphabet: # ignore any punctuation, numbers, etc
                if char in letter_count:
                        letter_count[char] = letter_count[char] + 1
                else:
                        letter_count[char] = 1

keys = letter_count.keys()
keys.sort()
for char in keys:
        print(char, letter_count[char])