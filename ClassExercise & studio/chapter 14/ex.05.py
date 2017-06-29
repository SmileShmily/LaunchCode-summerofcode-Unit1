'''Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:

r = Rectangle(Point(100, 50), 10, 5)
test(r.width, 10)
test(r.height, 5)
r.transpose()
test(r.width, 5)
test(r.height, 10)

'''

from test import testEqual

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)


class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH

    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp

#test methods
r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)