
''' how to put the loop code in for an RGB color that runs 100 different colors. '''

import turtle
turtle.setup(width=600, height=500)
turtle.bgcolor("blue")
turtle.reset()
turtle.hideturtle()
turtle.speed(0)
for i in range(1000):
   turtle.forward(i)
   turtle.right(98)

turtle.exitonclick()

'''
import colorsys
#turtle setup stuff goes here
for i in range(1000):
    idx = int(i/10)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(i)
    turtle.right(98)

    '''