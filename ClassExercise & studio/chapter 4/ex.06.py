'''Write a program that asks the user for the number of sides, the length of the side, the color,
 and the fill color of a regular polygon. The program should draw the polygon and then fill it in.
'''

import turtle

wn = turtle.Screen()

babbage = turtle.Turtle()
babbage.shape("triangle")

a= int(input("How many sides ? "))

b= int(input("The length of the side ? "))

#c= int(input("The color "))
angle = 360 / a

for i in range(a,b):
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

