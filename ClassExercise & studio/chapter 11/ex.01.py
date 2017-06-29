'''Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average.
'''
import random

def createRandList():
    newlist = []
    for i in range(100):
        newint = random.randrange(0,1001)
        newlist.append(newint)
    return newlist

def average(aList):
    totalitems = 0
    totalvalue = 0
    for item in aList:
        intitem = int(item)
        totalitems = totalitems + 1
        totalvalue = totalvalue + intitem
    averagevalue = totalvalue/totalitems
    return averagevalue

myList = createRandList()
listAverage = average(myList)

print(myList)
print(listAverage)
