'''Write a function called drawSprite that will draw a sprite.
 The function will need parameters for the turtle, the number of legs,
 and the length of the legs. Invoke the function to create a sprite with 15 legs of length 120.
'''

import turtle

def drawSprite(t, numlegs, leglength):
   angle = 360/numlegs
   for i in range(numlegs):
      t.forward(leglength)
      t.backward(leglength)
      t.left(angle)



wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawSprite(alex, 15, 120)

wn.exitonclick()
