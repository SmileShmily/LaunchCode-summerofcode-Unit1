'''Write a function that removes all occurrences of a string from another string.
'''

from test import testEqual

def remove_all(substr,theStr):
    # your code here
    new = theStr.replace(substr, "")
    return new
testEqual(remove_all('an', 'banana'), 'ba')
testEqual(remove_all('cyc', 'bicycle'), 'bile')
testEqual(remove_all('iss', 'Mississippi'), 'Mippi')
testEqual(remove_all('eggs', 'bicycle'), 'bicycle')