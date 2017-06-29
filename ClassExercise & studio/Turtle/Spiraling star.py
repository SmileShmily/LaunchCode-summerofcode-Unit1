'''Additional notes

Notice that now I’m moving the turtle forward by a different amount each time.
 What happens if instead of multiplying i by 10, I multiply it against itself? What if I do spiral.forward(i * i) instead?'''

import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()