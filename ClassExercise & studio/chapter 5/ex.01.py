'''Use the drawsquare function we wrote in this chapter in a program to draw the image shown below.
 Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last square
  when the program ends.)
../_images/five_squares.png '''

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

for i in range(5):
    drawSquare(alex, 20)   # Call the function to draw the square
    alex.penup()
    alex.forward(40)       # move alex to the starting position for the next square
    alex.pendown()

wn.exitonclick()
