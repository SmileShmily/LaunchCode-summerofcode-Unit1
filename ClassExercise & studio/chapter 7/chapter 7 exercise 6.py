'''Modify the previous turtle walk program so that the turtle turns around when it hits the wall or
 when one turtle collides with another turtle.
'''


import turtle
import random

def setStart(t):
    tx = random.randrange(-300,300,100)
    ty = random.randrange(-300,300,100)

    t.penup()
    t.goto(tx,ty)
    t.pendown()

def throwCoin(t):
    coin = random.randrange(0,2)

    if coin == 0:
        t.left(90)
    else:
        t.right(90)

def isInScreen(w,t):
    leftBound = w.window_width() / -2
    rightBound = w.window_width() / 2
    bottomBound = w.window_height() / -2
    topBound = w.window_height() / 2

    turtlex = t.xcor()
    turtley = t.ycor()

    stillIn = True

    if turtlex < leftBound or turtlex > rightBound or turtley < bottomBound or turtley > topBound:
        stillIn = False

    return stillIn

def collide(t,u):
    if abs(t.xcor() - u.xcor()) < 1 and abs(t.ycor() - u.ycor()) < 1:
        return True
    return False

def randomWalk(t,w):
        if not isInScreen(w,t):
            t.left(180)
        else:
            throwCoin(t)
        t.forward(100)

def doubleRandom(t,u,w):
    while not collide(t, u):
        randomWalk(t, w)
        if collide(t, u):
            break
        randomWalk(u, w)

wn = turtle.Screen()
wn.bgcolor('lightcyan')

steklovata = turtle.Turtle()
steklovata.color('darkslategray')
steklovata.shape('turtle')
setStart(steklovata)

catshower = turtle.Turtle()
catshower.color('orangered')
catshower.shape('turtle')
setStart(catshower)

doubleRandom(steklovata,catshower,wn)

wn.exitonclick()

