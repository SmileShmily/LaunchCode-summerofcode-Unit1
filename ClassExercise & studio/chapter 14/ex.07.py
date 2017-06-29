'''Write a new method called diagonal that will return the length of the diagonal that runs from the lower left corner to the opposite corner.
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

    def diagonal(self):

        d = (self.width**2 + self.height**2) ** 0.5
        return d

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.diagonal(), 11.1803398875)

r1 = Rectangle(Point(0,0), 12, 4)
testEqual(r1.diagonal(), 12.6491106407)

r2 = Rectangle(Point(0,0), 1,2)
testEqual(r2.diagonal(), 2.2360679775)
