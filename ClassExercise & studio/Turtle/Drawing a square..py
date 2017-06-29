'''Additional notes

The two turtle commands we’ve learned so far are forward(x),
which moves the turtle forward in the direction its facing by x number of pixels, and right(d),
 which makes it turn clockwise by d number of degrees.

Two additional key commands are backward(x), which makes the turtle move back, and left(d),
which makes the turtle turn counterclockwise by d degrees.

Exercise: try modifying writing code to draw a square using only the backward and left commands.'''

import turtle

silly = turtle.Turtle()

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()