'''Write a function that removes all occurrences of a given letter from a string.
'''
'''from test import testEqual


def remove_letter(theLetter, theString):
    # your code here
    new_theString = theString.replace(theLetter, "")
    return new_theString
# get user input for example
#b_str = raw_input("What string would you like to remove from?")
#a_str = raw_input("What would you like to remove from that string?")
#print(remove_all(a_str, b_str))'''

#testEqual(remove_letter('a', 'apple'), 'pple')
#testEqual(remove_letter('a', 'banana'), 'bnn')
#testEqual(remove_letter('z', 'banana'), 'banana')'''

from test import testEqual
import math


def is_rightangled(a, b, c):
    sumSquaredSides = (a ** 2 + b ** 2)
    squaredHypot = c ** 2
    if abs(sumSquaredSides - squaredHypot) < 0.001:
        return (True)
    return (False)


testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)



