'''What is printed by the following statements?
'''

alist = [4, 2, 8, 6, 5]
temp = alist.pop(2)
temp = alist.pop()
print(alist)
'''Correct! Yes, first the 8 was removed, then the last item, which was 5.'''
alist = [4, 2, 8, 6, 5]
alist = alist.pop(0)
print(alist)
'''Correct! Yes, first the 4 was removed from the list, then returned and assigned to alist. The list is lost.'''
'''alist = [4, 2, 8, 6, 5]
alist = alist + 999
print(alist)'''
'''Correct! Yes, in order to perform concatenation you would need to write alist+[999]. You must have two lists.'''
'''Lists and for loops
It is also possible to perform list traversal using iteration by item as well as iteration by index.
'''
fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit)
'''It almost reads like natural language: For (every) fruit in (the list of) fruits, print (the name of the) fruit.

We can also use the indices to access the items in an iterative fashion.'''

fruits = ["apple", "orange", "banana", "cherry"]

for position in range(len(fruits)):  # by index
    print(fruits[position])

'''Any sequence expression can be used in a for loop. For example, the range function returns a sequence of integers.'''
for number in range(20):
    if number % 3 == 0:
        print(number)
'''Since lists are mutable, it is often desirable to traverse a list, modifying each of its elements as you go.
 The following code squares all the numbers from 1 to 5 using iteration by position.'''
numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)
'''What is printed by the following statements?'''
alist = [4, 2, 8, 6, 5]
blist = [ ]
for item in alist:
    blist.append(item+5)
print(blist)
