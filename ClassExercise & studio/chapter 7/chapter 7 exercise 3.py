#方法一
'''def is_prime(n):
    """
    Prime Numbers. We presented some code in this chapter to determine a number's
    largest factor or if it is prime. Turn this code into a Boolean function called isprime()
    such that the input is a single value, and the result returned is true if the number is
    prime and False otherwise.
    """
    if n == 1:
        return False
    f = n/2
    while f > 1:
        # print f
        if n%f == 0:
            return  False
            break
        f -= 1
    else:
        return True
print(is_prime(15))
print(is_prime(4))'''
#方法二
'''
def isprime(n=936):
    """Write a function, is_prime, that takes a single integer argument and
    returns True when the argument is a prime number and False otherwise."""
    if n < 3: return False
    for i in range(2, n):
        if n % i == 0:
            return False
            return True
            '''

#方法三
'''
def is_prime(n):
    """
    Prime Numbers. We presented some code in this chapter to determine a number's
    largest factor or if it is prime. Turn this code into a Boolean function called isprime()
    such that the input is a single value, and the result returned is true if the number is
    prime and False otherwise.
    """
    if n == 1:
        return False
    f = n/2
    while f > 1:
        # print f
        if n%f == 0:
            return  False
            break
        f -= 1
    else:
        return True
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
'''

#方法四
'''
def is_prime(n):
    x = n - 1

    # if n is less than 2, its 0/1
    # which is not conventionally a prime number
    if n < 2:
        return False

    # if n is 2 then its a prime number!
    if n == 2:
        return True

    while x > 1:
        if n % x == 0:
            return False
        else:
            x -= 1
    return True
    '''
#方法五
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(25))
print(is_prime(7))
print(is_prime(251))
print(is_prime(20))