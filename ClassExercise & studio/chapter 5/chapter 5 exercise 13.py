# Write a function called mySqrt that will approximate the
# square root of a number, call it n, by using Newton’s
# algorithm. Newton’s approach is an iterative guessing
# algorithm where the initial guess is n/2 and each subsequent
# guess is computed using the formula:
# newguess = (1/2) * (oldguess + (n/oldguess)).


def mySqrt(n):
    oldguess = n / 2.0

    for i in range(6):
        newguess = (1 / 2) * (oldguess + (n / oldguess))
        oldguess = newguess
    return newguess


print(mySqrt(2))
print(mySqrt(4))
print(mySqrt(5))
print(mySqrt(144))
print(mySqrt(444))
print(mySqrt(987654321))