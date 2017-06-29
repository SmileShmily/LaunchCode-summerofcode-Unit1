"""Modify the turtle bar chart program from the previous chapter so that the
    bar for any value of 200 or more is filled with red, values between
    [100 and 200) are filled yellow, and bars representing values less than 100
    are filled green."""

import turtle
from random import randint

wn = turtle.Screen()
wn.delay(0.1)
t = turtle.Turtle()
t.color("blue")
t.left(90)
n=100
for i in range(n):
    x = randint(-100, 250)
    if x >= 200:
        t.fillcolor("red")
    elif 100 <= x < 200:
        t.fillcolor("yellow")
    elif 0 <= x < 100:
        t.fillcolor("green")
    else:
        t.fillcolor("orange")
    t.begin_fill()
    if x <= 0: t.write(x)
    t.forward(x)
    t.right(90)
    if x > 0: t.write(x)
    t.forward(20)
    t.left(90)
    t.forward(-x)
    t.end_fill()
t.color("blue")
t.left(90)
t.forward(n * 20)
wn.exitonclick()