'''A method behaves like a function but it is invoked on a specific instance.
 For example, with a turtle named tess, tess.right(90) asks the tess object to perform its right method and turn 90 degrees.
  Methods are accessed using dot notation.
'''


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


p = Point(7, 6)
print(p.getX())
print(p.getY())










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


p = Point(7, 6)
print(p.distanceFromOrigin())