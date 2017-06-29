'''Write a recursive function to compute the factorial of a number.
'''
'''
#fangfa 1
def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       return n * factorial( n - 1 )  # recursive call
def fact(n):
       for i in range(1, n+1 ):
               print ("%2d! = %d" % ( i, factorial( i ) ))
print(factorial( 5 ))
'''
#fangfa 2
def fractorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fractorial(num - 1)
print(fractorial(0))
print(fractorial(1))
print(fractorial(5))
print(fractorial(10))

#fangfa 3
def fac(n):
    return 1 if (n < 1) else n * fac(n - 1)
print(fac(4))