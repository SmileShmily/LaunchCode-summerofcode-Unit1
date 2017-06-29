'''Write a program to draw this. Assume the innermost square is 20 units per side,
 and each successive square is 20 units bigger, per side, than the one inside it.
../_images/nested_squares.png '''

import turtle
def createWindow(bgcolor, title):
   w = turtle.Screen()
   w.bgcolor(bgcolor)
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