'''For example, if you say, Chris and I have the same car, you mean that his car and yours are the same make and model,
but that they are two different cars. If you say, Chris and I have the same mother, you mean that his mother and yours are the same person.

When you talk about objects, there is a similar ambiguity. For example,
if two Fractions are the same, does that mean they contain the same data (same numerator and denominator) or that they are actually the same object?

We’ve already seen the is operator in the chapter on lists, where we talked about aliases.
 It allows us to find out if two references refer to the same object.
'''

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)

ourfraction = myfraction
print(myfraction is ourfraction)



'''This type of equality is called shallow equality because it compares only the references, not the contents of the objects.
Using the == operator to check equality between two user defined objects will return the shallow equality result.
In other words, the Fraction objects are equal (==) if they are the same object.

Of course, we could define equality to mean the fractions are the same in that they have the same numerator and the same denominator.
 For example, here is a boolean function that performs this check.

def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

This type of equality is known as deep equality since it compares the values “deep” in the object, not just the reference to the object.
'''
def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print(sameFraction(myfraction, yourfraction))