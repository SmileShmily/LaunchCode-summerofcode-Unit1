'''Our add method will take a Fraction as a parameter. It will return a new Fraction representing the sum.
We will use the equation shown above to compute the new numerator and the new denominator.
Since this equation will not give us lowest terms, we will utilize a similar technique as was used in the simplify method to find the greatest common divisor and then divide each part of the new fraction.

def add(self,otherfraction):

    newnum = self.num*otherfraction.den + self.den*otherfraction.num
    newden = self.den * otherfraction.den

    common = gcd(newnum,newden)

    return Fraction(newnum//common,newden//common)

You can try the addition method and then modify the fractions and retry.
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

    def add(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

f3 = f1.add(f2)
print(f3)
