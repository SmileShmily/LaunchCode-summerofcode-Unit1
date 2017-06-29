'''A sprite is a simple spider shaped thing with n legs coming out from a center point. The angle between each leg is 360 / n degrees.

Write a program to draw a sprite where the number of legs is provided by the user.
'''

import turtle

wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("triangle")

n = int(input("How many legs should this sprite have? "))
angle = 360 / n

for i in range(n):
    # draw the leg
    babbage.right(angle)
    babbage.forward(65)
    babbage.stamp()

    # go back to the middle and turn back around
    babbage.right(180)
    babbage.forward(65)
    babbage.right(180)

babbage.shape("circle")

wn.exitonclick()
