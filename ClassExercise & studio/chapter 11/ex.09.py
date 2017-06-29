'''Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

Hint: use the split and join methods.
'''

#solve 1
'''
from test import testEqual
def replace(s, old, new):
    wds = s.split(old)
    glue = new
    new = glue.join(wds)
    return new

testEqual(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
testEqual(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

testEqual(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
'''


#solve 2
def replace(thStr,old,new):
    strList=[]
    strList = thStr.split(old)
    newStr=new.join(strList)
    return(newStr)

print(replace('Mississippi', 'i', 'I'))

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
print(replace(s, 'om', 'am'))

print(replace(s, 'o', 'a'))