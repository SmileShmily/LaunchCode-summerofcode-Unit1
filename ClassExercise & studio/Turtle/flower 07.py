import turtle
from random import randint

# set the background color
wn = turtle.Screen()
wn.clear()
wn.bgcolor("yellow")


def drawSquare(turtle, size, pos):
    # initialize position
    turtle.up()
    turtle.setpos(pos)
    turtle.down()

    # for loops iterate in this case from the first value until < 4, so
    for i in range(0, 4):
        turtle.forward(size)
        turtle.right(90)


t = turtle.Pen()
t.shape("turtle")
t.color("red")

s = turtle.Pen()
s.shape("turtle")
s.color("green")

# draw squares
drawSquare(t, 50, (100, 0))
drawSquare(s, 50, (-100, 0))
turtle.exitonclick()
