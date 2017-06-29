'''The dot operator can also be used to access built-in methods of list objects.
append is a list method which adds the argument passed to it to the end of the list.
Continuing with this example, we show several other list methods. Many of them are easy to understand.
'''



mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)
