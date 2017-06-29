# Spiral outwards in an ever-expanding square
#   using Turtle graphics

from turtle import *

lineLen = inc = 20  # Line starts this long, grows this much
max = 800  # until it's this long
turn = 90  # try different numbers, e.g. 120

#   The line grows longer until it fills the window
while lineLen < max:
    #turtle.forward
    forward(lineLen)
    #turtle.right
    right(turn)
    lineLen += inc

#turtle.done
done()