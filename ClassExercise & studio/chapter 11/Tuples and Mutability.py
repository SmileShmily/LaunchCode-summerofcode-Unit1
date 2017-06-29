'''So far you have seen two types of sequential collections: strings, which are made up of characters; and lists,
 which are made up of elements of any type. One of the differences we noted is that the elements of a list can be modified,
  but the characters in a string cannot. In other words, strings are immutable and lists are mutable.

A tuple, like a list, is a sequence of items of any type. Unlike lists, however, tuples are immutable.
 Syntactically, a tuple is a comma-separated sequence of values.
  Although it is not necessary, it is conventional to enclose tuples in parentheses:

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

'''

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)
