'''Write a program to draw a face of a clock that looks something like this:
../_images/tess_clock1.png '''

import turtle

wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("turtle")

angle = 360 / 12

for i in range(12):
    # draw the hour
    babbage.right(angle)
    babbage.forward(65)
    babbage.stamp()

    # go back to the middle and turn back around
    babbage.right(180)
    babbage.forward(65)
    babbage.right(180)

babbage.shape("turtle")

wn.exitonclick()



