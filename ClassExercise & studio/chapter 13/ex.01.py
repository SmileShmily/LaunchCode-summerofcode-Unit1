'''Add a distanceFromPoint method that works similar to distanceFromOrigin except that it takes a Point as a parameter and computes the distance between that point and self.
'''

import math

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

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

p = Point(3, 3)
q = Point(6, 7)
print(p.distanceFromPoint(q))