'''Let us show another use of this pattern. Assume you already have a function is_prime(x) that can test if x is prime.
Now, write a function to return a list of all prime numbers less than n:
'''

def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result