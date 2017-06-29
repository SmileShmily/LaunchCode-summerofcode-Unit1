'''    )

    (GRADED) Write a function that mirrors its argument.

(Hint: Make use of the reverse function that you wrote in the previous exercise)

'''

from test import testEqual
def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed
def mirror(mystr):
    # your code here
    return mystr + reverse(mystr)
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')