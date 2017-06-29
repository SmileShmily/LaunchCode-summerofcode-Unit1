'''The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”).
The coefficients a and b completely describe the line.
 Write a method in the Point class so that if a point instance is given another point,
 it will compute the equation of the straight line joining the two points.
 It must return the two coefficients as a tuple of two values. For example,

#>>> print(Point(4, 11).get_line_to(Point(6, 15)))
#>>> (2, 3)

This tells us that the equation of the line joining the two points is “y = 2x + 3”. When will your method fail?
'''


def move(self, units):
    """Add a method called move that will take two parameters, call them dx
    and dy. The method will cause the point to move in the x and y direction
    the number of units given."""
    self.x += units
    self.y += units
