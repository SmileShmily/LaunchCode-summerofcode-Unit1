'''Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).
'''

import turtle

def drawStar(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)

stroustrup = turtle.Turtle()
drawStar(stroustrup, 7)
