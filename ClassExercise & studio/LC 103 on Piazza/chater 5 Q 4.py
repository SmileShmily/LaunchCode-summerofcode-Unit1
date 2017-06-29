import turtle

wn = turtle.Screen()
wn.bgcolor("light green")

alex = turtle.Turtle()
alex.pencolor("blue")
alex.penup()
alex.goto(-100,0)
alex.pendown()
alex.speed(10)
alex.right(90)

ayden = turtle.Turtle()
ayden.pencolor("blue")
ayden.penup()
ayden.goto(100,0)
ayden.pendown()
ayden.speed(10)
ayden.right(90)

def drawSpiral(turtle,sides, angle, length):
     for i in range(sides):
          length = length + 2
          alex.forward(length)
          alex.right(angle)

drawSpiral(alex, 50, 90, 2)

drawSpiral(ayden,50, 89, 2)

wn.exitonclick()

'''
def drawSpiral(turtle,sides, angle, length):
for i in range(sides):
length = length + 2
alex.forward(length)
alex.right(angle)
'''