'''Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing of all the words, and the number of times each occurs, in the text version of Alice’s Adventures in Wonderland. (You can obtain a free plain text version of the book, along with many others, from http://www.gutenberg.org.)
The first 10 lines of your output file should look something like this
    Word
    Count
    a
    631
    a-piece
    1
    abide
    1
    able
    1
    about
    94
    above
    3
    absence
    1
    absurd
    2

How many times does the word, alice, occur in the book?
If you are writing this in the activecode window simply print out the results rather than write them to a file.'''

f = open('alice.txt', 'r')

count = {}

for line in f:
    for word in line.split():
        # remove punctuation
        word = word.replace('_','').replace('"','').replace(',','').replace('.','')
        word = word.replace('-','').replace('?','').replace('!','').replace("'","")
        word = word.replace('(','').replace(')','').replace(':','').replace('[','')
        word = word.replace(']','').replace(';','')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")