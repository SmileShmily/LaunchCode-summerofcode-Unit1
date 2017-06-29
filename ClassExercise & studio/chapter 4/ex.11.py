'''Write a program to draw some kind of picture. Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.


'''

import turtle

tanenbaum = turtle.Turtle()

tanenbaum.hideturtle()
tanenbaum.speed(20)

for i in range(350):
    tanenbaum.forward(i)
    tanenbaum.right(98)

