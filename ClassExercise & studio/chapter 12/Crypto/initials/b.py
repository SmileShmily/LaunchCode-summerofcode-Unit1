''' Description:
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
The string can contains any char.
Examples input/output:
[python] view plain copy
print?在CODE上查看代码片派生到我的代码片

    xo("ooxx") => true
    xo("xooxx") => false
    xo("ooxXm") => true
    xo("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    xo("zzoo") => false  '''


def xo(s):
    return s.lower().count('x') == s.lower().count('o')
print(xo("ooxx"))
print( xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))