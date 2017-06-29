'''Write a function called fancySquare that will draw a square with fancy corners (spites on the corners).
You should implement and use the drawSprite function from above.
 For an even more interesting look, how about adding small triangles to the ends of the sprite legs.
'''

import turtle

def drawSprite(t, numlegs, leglength):
   angle = 360/numlegs
   for i in range(numlegs):
      t.forward(leglength)
      t.backward(leglength)
      t.left(angle)

def drawFancySquare(t, sz, lgs, lgl):
   for i in range(4):
       t.forward(sz)
       drawSprite(t, lgs, lgl)
       t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawFancySquare(alex, 100, 10, 15)

wn.exitonclick()
