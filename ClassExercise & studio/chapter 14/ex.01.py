'''We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a Rectangle class using this idea. To create a Rectangle object at location (4,5) with width 6 and height 5, we would do the following:

r = Rectangle(Point(4, 5), 6, 5)

'''

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

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r)
