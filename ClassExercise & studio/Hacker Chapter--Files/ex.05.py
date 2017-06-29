'''At the bottom of this page is a very long file called mystery.txt The lines of this file contain either the word UP or DOWN or a pair of numbers.
 UP and DOWN are instructions for a turtle to lift up or put down its tail. The pairs of numbers are some x,y coordinates.
 Write a program that reads the file mystery.txt and uses the turtle to draw the picture described by the commands and the set of points.
'''

import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)

f = open("mystery.txt", "r")

for aline in f:
    items = aline.split()
    if items[0] == "UP":
        t.up()
    else:
        if items[0] == "DOWN":
            t.down()
        else:
            # must be coords
            t.goto(int(items[0]), int(items[1]))

f.close()
wn.exitonclick()
