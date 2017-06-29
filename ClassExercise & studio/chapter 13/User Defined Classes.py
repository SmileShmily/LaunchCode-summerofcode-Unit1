'''Every class should have a method with the special name __init__.
This initializer method, often referred to as the constructor, is automatically called whenever a new instance of Point is created.
It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values.
The self parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly-created object
that needs to be initialized.

So let’s use our new Point class now.
'''
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print("Nothing seems to have happened with the points")





class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)
