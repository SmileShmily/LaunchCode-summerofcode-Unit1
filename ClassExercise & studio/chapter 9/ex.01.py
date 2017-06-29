'''In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are
Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)

Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?

'''
prefixes = 'JKLMNOPQ'
suffix = 'ack'
suffix2 = 'auck'
a = 0

while a < len(prefixes):
    letter = prefixes[a]
    if (letter == "O"):
        print(letter + suffix2)
    elif (letter == "Q"):
        print(letter + suffix2)
    else:
        print(letter + suffix)
    a += 1

