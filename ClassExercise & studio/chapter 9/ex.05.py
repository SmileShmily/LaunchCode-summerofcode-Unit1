'''Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).
'''
from test import testEqual

def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed

def is_palindrome(myStr):
    if myStr in reverse(myStr):
        return True
    else:
        return False

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)