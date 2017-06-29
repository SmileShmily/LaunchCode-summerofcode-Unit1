'''Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
'''

'''
def reflect(self):
    """Add a method reflect_x to Point which returns a new Point, one which
    is the reflection of the point about the x-axis. For example,
    Point(3, 5).reflect_x() is (3, -5)"""
    return self.x, -self.y
'''



class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return '({0} , {1})'.format(self.x,self.y)
    def reflect_x(self):
        return Point(self.x,-self.y)

p1=Point(3,4)
p2=p1.reflect_x

print(str(p1),str(p2))
print(type(p1),type(p2))
