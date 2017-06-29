'''Write a program to draw this. Assume the innermost square is 20 units per side,
and each successive square is 20 units bigger, per side, than the one inside it.
../_images/nested_squares.png '''



'''import turtle

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

size=20
for i in range(5):
    size=size+20
    drawSquare(alex, size)   # Call the function to draw the square
    alex.penup()
    alex.goto(size,size)       # move alex to the starting position for the next square
    alex.pendown()

wn.exitonclick()
'''

import turtle
def createWindow(bgcolor, title):
   w = turtle.Screen()
   w.bgcolor(bgcolor)
   w.title(title)
   return w
def createTurtle(color, size):
   t = turtle.Turtle()
   t.pensize(size)
   t.color(color)
   return t

def jump(t, l):
   t.penup()
   t.backward(l)
   t.right(90)
   t.forward(l)
   t.left(90)
   t.pendown()

def draw_square(t, l):
    for i in range(4):
        t.forward(l)
        t.left(90)
    jump(t, 10)
wn = createWindow("lightgreen", "Exercises 4.2")
tess = createTurtle("hotpink", 3)
for i in range(5):
    draw_square(tess, 20 * (i + 1))
wn.mainloop()

