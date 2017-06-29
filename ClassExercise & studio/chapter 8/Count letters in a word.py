'''def has_no_e(word):     #counts 'e's in a word
    letters = len(word)
    count = 0
    while letters >= 0:
        if word[letters-1] == 'e':
            count = count + 1
        letters = letters - 1
    print (count)'''

def count_letter(word, char='e'):
    count = 0
    for c in word:
         if c == char:
                count += 1
    return count
print(count_letter('tee'))
print(count_letter('tee', 't'))
print(count_letter('tee', 'f'))
print(count_letter('wh' + 'e'*100))
'''

You don't have to use a while-loop. Strings can be used for-loops in Python.

def has_no_e(word):
    count = 0
    for letter in word:
        if letter == "e":
            count += 1
    print count

or something simpler:

def has_no_e(word):
    return sum(1 for letter in word if letter=="e")

'''

