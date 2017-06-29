'''Add a method area to the Rectangle class that returns the area of any instance:

r = Rectangle(Point(0, 0), 10, 5)
test(r.area(), 50)

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

    def area(self):
        return self.width * self.height

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)

r1 = Rectangle(Point(0,0), 4, 5)
testEqual(r1.area(), 20)

r2 = Rectangle(Point(0,0), 12, 3)
testEqual(r2.area(), 36)
