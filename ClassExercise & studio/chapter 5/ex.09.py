'''Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 350 units,
turn right by 144, put the pen down, and draw the next star.
 You’ll get something like this (note that you will need to move to the left before drawing your first star in order to
  fit everything in the window):
../_images/five_stars.png
What would it look like if you didn’t pick up the pen?
'''
import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(30)
        t.left(216)
        t.color("hotpink")


wolfram = turtle.Turtle()
drawFivePointStar(wolfram)


wolfram.penup()
wolfram.forward(100)
wolfram.right(144)
wolfram.pendown()
wolfram.color("hotpink")
for i in range(5):
        wolfram.forward(30)
        wolfram.left(216)


