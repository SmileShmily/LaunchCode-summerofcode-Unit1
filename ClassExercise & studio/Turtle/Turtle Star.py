#   Turtle Star
#   Turtle can draw intricate shapes using programs that repeat simple moves.

from turtle import *

size = 790
color('green', 'blue')
speed('fastest')
setpos(-size / 2, -32)
start = pos()  # Note starting position
begin_fill()
while True:
    forward(size)
    left(170)
    if abs(pos() - start) < 1:  # have we come back to start?
        break
end_fill()
done()