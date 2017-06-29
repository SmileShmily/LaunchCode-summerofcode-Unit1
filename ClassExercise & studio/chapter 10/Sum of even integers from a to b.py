def sum_even(a, b):
    return sum(i for i in range(a, b + 1) if i % 2 == 0)
print(sum_even(3,7))


'''As NPE pointed out, my original solution above uses floating-point maths.
I wasn't too concerned, since the overhead of floating-point maths is negligible compared with the removal of the looping (e.g. if calling sum_even(10, 10000)).
Furthermore, the calculations use (negative) powers of two, so shouldn't be subject by rounding errors.

Anyhow, with the simple trick of multiplying everything by 4 and then dividing again at the end we can use integers throughout, which is preferable.'''
def sum_even(a, b):
    if (a % 2 == 1):
        a += 1
    if (b % 2 == 1):
        b -= 1
    return (a * (2 - a) + b * (2 + b)) / 4
print(sum_even(3,7))



'''I'd like you see how your loops work if b is close to 2^32 ;-) As Matthew said there is no loop needed but he does not explain why.

The problem is just simple arithmetic sequence wiki. Sum of all items in such sequence is:

      (a+b)
Sn = ------- * n
        2

where 'a' is a first item, 'b' is last and 'n' is number if items. If we make 'a' and b' even numbers we can easily solve given problem. So making 'a' and 'b' even is just:

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
print(sum_even(3,7))