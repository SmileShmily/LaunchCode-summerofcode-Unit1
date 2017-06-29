
'''from collections import Counter
import string


def count_letters(word):
    global count
    wordsList = string.split(word)
    count = Counter()
    for words in wordsList:
        for letters in set(words):
            return count[letters]

word = "The grey old fox is an idiot"
print(count_letters(word))'''
def count_dict(mystring):
    d = {}
# count occurances of character
    for w in mystring:
        d[w] = mystring.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

mystring='qwertyqweryyyy'
count_dict(mystring)