
'''Add the following accessor methods to the Rectangle class: getWidth, getHeight, __str__.
'''



class Point:

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

    def __init__(self, initP, initW, initH):

        self.__location = initP
        self.__width = initW
        self.__height = initH



    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getLocation(self):
        return self.__location

    #---------------------------------------------------------------
    #string

    def __str__(self):
        return "x=" + str(self.__location.x) + ", y=" + str(self.__location.y) +", Width=" + str(self.getWidth()) + ", Height=" +str(self.getHeight())

    def area(self):
        return self.getWidth() * self.getHeight()

    def calculatePerimeter(self):
        return self.getWidth()*2 +self.getHeight()*2

    def transpose(self):
        temp = self.__width
        self.__width = self.__height
        self.__height = temp

    def encloses(self, otherP):
        return ((self.getWidth() + self.getLocation().getX()) > otherP.getX()\
               and (self.getLocation().getX()) <otherP.getX() \
               and (self.getHeight() + self.getLocation().getY()) >otherP.getY()\
               and self.getLocation().getY() < otherP.getY())

    def computeDiagonal(self):

        d = (self.getWidth()**2 + self.getHeight()**2) ** 0.5
        return d

    def detectCollision(firstRectangle, secondRectangle):
        print(firstRectangle.getWidth())
        print(secondRectangle)


first = Rectangle(Point(1,0), 4, 3)
second = Rectangle(Point(4,0), 4, 3)
Rectangle.detectCollision(first, second)

