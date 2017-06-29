'''The previous example creates a list from a sequence of values based on some selection criteria.
An easy way to do this type of processing in Python is to use a list comprehension.
List comprehensions are concise ways to create lists. The general syntax is:

[<expression> for <item> in <sequence> if  <condition>]

where the if clause is optional. For example,
'''
mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)


alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)
'''Correct! Yes, 5 is the only odd number in alist. It is doubled before being placed in blist.'''
