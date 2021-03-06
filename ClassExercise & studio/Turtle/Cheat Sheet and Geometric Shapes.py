# "A black and red triangle"
'''
import turtle

turtle.pen(fillcolor="black", pencolor="red", pensize=10)
turtle.fill(True)
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.fill(False)
'''


'''
# "A spiral out of squares"
import turtle

size = 1
while (True):
    turtle.forward(size)
    turtle.right(91)
    size = size + 1
'''

'''
# "A nautilus shape"
import turtle

size = 1
while (True):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        size = size + 1
    turtle.right(10)
'''

'''
# "A yellow star pattern"
import turtle

turtle.pen(pencolor='red', fillcolor='yellow')
turtle.fill(True)
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.fill(False)
turtle.done()
'''
# "Recursive Star"
import turtle


def star(turtle, n, r):
    """ draw a star of n rays of length d"""
    for k in range(0, n):
        turtle.pendown()
        turtle.forward(r)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360 / n)


def recursive_star(turtle, n, r, depth, f):
    """At each point of the star, draw another smaller star,
    and so on, up to given depth. Rescale the stars by a factor f
    at each generation."""

    if depth == 0:
        star(turtle, n, f * 4)
    else:
        for k in range(0, n):
            turtle.pendown()
            turtle.forward(r)
            recursive_star(turtle, n, f * r, depth - 1, f)
            turtle.penup()
            turtle.backward(r)
            turtle.left(360 / n)


fred = turtle.Turtle()
fred.speed("fastest")
recursive_star(fred, 5, 150, 4, 0.4)