'''
Chapter 9 Assignment
Write a function that receives a string argument, and returns a "mirrored" version of the string.
'''
# TODO
# write a function, mirror, that receives a string and returns a mirrored version
# first implement a function, reverse, which receives a string and returns a reversed version
# next, implement the mirror function (and make use of your reverse function)


def mirror(text):
    # your code here
    return text + reverse(text)

def reverse(text):
    # your code here
    reversed = ''
    for char in text:
        reversed = char + reversed
    return reversed
  #  [Executed at: Sat  Jul 2 13:20:06 PDT 2016]
  #1 Your  code  passed  all the tests!
