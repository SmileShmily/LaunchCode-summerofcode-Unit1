'''    )

    (GRADED) Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For example,

    #>>> Point(4, 10).slope_from_origin()
    2.5

What cases will cause your method to fail? Return None when it happens.
'''
from test import testEqual

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # TODO define a method called slopeFromOrigin here
    def slopeFromOrigin(self):
        """Add a method slope_from_origin which returns the slope of the line
        joining the origin to the point."""
        if self.x:
                return self.y/self.x

p = Point(4, 10)
testEqual(p.slopeFromOrigin(), 2.5)
