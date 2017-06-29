'''Write a function that removes the first occurrence of a string from another string.
'''

from test import testEqual

def remove(substr,theStr):
    # your code here
    index =theStr.find(substr);
    if index==-1:
        return theStr
    if index>=0:
        return theStr[:index] + theStr[index+len(substr):]
testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
