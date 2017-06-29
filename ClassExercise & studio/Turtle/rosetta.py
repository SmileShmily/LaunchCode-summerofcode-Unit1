"""Draw rosetta figure using pentagons."""
from turtle import *
fred = Turtle()
fred.speed("fast")

def pentagon(turtle):
    for k in range(0 ,5):
        turtle.forward(100)
        turtle.left(72)

def repeat(figure, turtle, n, angle):
    for k in range(0 ,n):
        figure(turtle)
        turtle.left(angle)
    turtle.penup()
    turtle.forward(200)

def saveImage(turtle, filename):
    ts = turtle.getscreen()
    tc = ts.getcanvas()
    tc.postscript(file=filename)

def run(filename):
    repeat(pentagon, fred, 20, 360/ 20)
    saveImage(fred, filename)
    exitonclick()


if __name__ == "__main__":
    run("rosetta5-20.eps")