'''Additional notes

What if you want different colors?
You could always try and guess what colors the turtle module can support, but if you want to be precise, you can use this colorpicker instead.

At the top of the screen, the website will provide a ‘#’ mark and a sequence of 6 letters or numbers that represents the color.
The turtle module will accept colors in this format.'''

import turtle

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123)  # Let's go counterclockwise this time

painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

turtle.done()