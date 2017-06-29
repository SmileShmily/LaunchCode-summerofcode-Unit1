
'''One place where this type of modification makes sense is when we place a fraction in lowest terms.
 Lowest terms simply means that the numerator and denominator do not share any common factors. For example,
 12/16 is a fraction but it is not in lowest terms since 2 can divide into both 12 and 16. We call 2 a common divisor.
  If we divide the numerator and the denominator by a common divisor, we get an equivalent fraction.
  If we divide by the greatest common divisor, we will get the lowest terms representation.
  In this case 4 would be the greatest common divisor and the lowest terms representation would be 3/4.
'''

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

print(gcd(12, 16))

'''Now that we have a function that can help us with finding the greatest common divisor,
 we can use that to implement a fraction method called simplify. We will ask the fraction “to put itself in lowest terms”.

The simplify method will pass the numerator and the denominator to the gcd function to find the greatest common divisor.
It will then modify itself by dividing its num and its den by that value.
'''

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

myfraction = Fraction(12, 16)

print(myfraction)
myfraction.simplify()
print(myfraction)
