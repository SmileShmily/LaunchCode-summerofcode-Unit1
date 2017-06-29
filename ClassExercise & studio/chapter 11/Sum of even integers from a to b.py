'''The problem is just simple arithmetic sequence wiki. Sum of all items in such sequence is:

      (a+b)
Sn = ------- * n
        2

where 'a' is a first item, 'b' is last and 'n' is number if items.
If we make 'a' and b' even numbers we can easily solve given problem.
So making 'a' and 'b' even is just:

if ((a & 1)==1):
    a = a + 1
if ((b & 1)==1):
    b = b - 1

Now think how many items do we have between two even numbers - it is:

    b-a
n = --- + 1
     2

Put it into equation and you get:

      a+b       b-a
Sn = ----- * ( ------ + 1)
       2         2
'''

def sum_even(a,b):
    if ((a & 1)==1):
        a = a + 1
    if ((b & 1)==1):
        b = b - 1
    return ((a+b)/2) * (1+((b-a)/2))

#Of course you may add some code to prevent a be equal or bigger than b etc.

#The sum of all the even numbers between the start and end number (inclusive).
 def addEvenNumbers(start,end):
  total = 0
  if end%2==0:
    for x in range(start,end):
      if x%2==0:
        total+=x
    return total+end
  else:
    for x in range(start,end):
      if x%2==0:
        total+=x
    return total
print (addEvenNumbers(4,12))


