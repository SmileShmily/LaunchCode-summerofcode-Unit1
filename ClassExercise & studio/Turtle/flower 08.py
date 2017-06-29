import turtle
from turtle import *
def part( total, length, breadth, col ):
    angleInc = 360/total
    width( breadth )
    color( col )
    for i in range(total):
        forward( length )
        left( angleInc )
def rosette( total, length, width, color, angleInc ):
    for i in range( 360/angleInc ):
        part( total, length, width, color )
        left( angleInc )

# set up the turtle
turtle.setup( 300, 300, 20, 20 ) # specify width, height, position on screen
turtle.speed(0) # draw as fast as possible

# call the functions
rosette(10,40,1,"blue",36)
rosette(5,80,1,"red",36)
turtle.exitonclick()