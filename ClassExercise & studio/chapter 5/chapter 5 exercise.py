'''chapter 5 exercise 1'''
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     # create alex
alex.color('hotpink')
alex.pensize(3)

for i in range(5):
    drawSquare(alex, 20)   # Call the function to draw the square
    alex.penup()
    alex.forward(40)       # move alex to the starting position for the next square
    alex.pendown()

wn.exitonclick()
'''chapter 5 exercise 3'''

import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)


'''import turtle

polygon = turtle.Turtle()
polygon.color("#FF69B4")
polygon.pensize(3)

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()'''

'''chapter 5 exercise 4'''
import turtle

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

guido = turtle.Turtle()    # create guido
guido.color('blue')

## draw the first spiral ##
# position guido
guido.penup()
guido.backward(110)
guido.pendown()

# draw the spiral using a 90 degree turn angle
drawSpiral(guido, 90)


## draw the second spiral ##
# position guido
guido.home()
guido.penup()
guido.forward(90)
guido.pendown()

drawSpiral(guido, 89)


'''exercise 6'''
from test import testEqual

def sumTo(n):
    result = (n * (n + 1)) / 2
    return result

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)


'''exercise 8'''
import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wolfram = turtle.Turtle()
drawFivePointStar(wolfram)

'''exercise 10'''
import turtle

def drawStar(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)

stroustrup = turtle.Turtle()
drawStar(stroustrup, 7)


'''exercise 12'''
def sumTo(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

# Now lets see how well this works
t = sumTo(0)
print("The sum from 1 to 0 is",t)
t = sumTo(10)
print("The sum from 1 to 10 is",t)
t = sumTo(5)
print("The sum from 1 to 5 is",t)

'''exercise 14'''

def myPi(iters):
    ''' Calculate an approximation of PI using the Leibniz
    approximation with iters number of iterations '''
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1  # alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx)


'''exercise 16'''
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








'''import turtle
import time
#定义绘制时画笔的颜色
turtle.color("purple")
#定义绘制时画笔的线条的宽度
turtle.pensize(5)
#定义绘图的速度
turtle.speed(10)
#以0,0为起点进行绘制
turtle.goto(0,0)
#绘出正方形的四条边
for i in range(4):
   turtle.forward(100)
   turtle.right(90)
#画笔移动到点(-150,-120)时不绘图
   turtle.up()
   turtle.goto(-150,-120)
#再次定义画笔颜色
   turtle.color("red")
#在(-150,-120)点上打印"Done"
   turtle.write("Done")
   time.sleep(3)

   '''

'''from turtle import *
import time

# pen/turtle starts at the center (x=0, y=0) of the turtle display area

color("green")
# pen up, don't draw
up()
# centers the circle
goto(0, -50)
# pen down, draw
down()
# radius=50  center is 50 radius units above the turtle
circle(50)
up()
# center the turtle again
goto(0, 0)
down()

# draw blue 100x100 squares
color("blue")
for deg in range(0, 61, 6):
    right(90 + deg)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

up()
goto(-150, -120)
color("red")
write("Done!")

time.sleep(5)  # wait 5 seconds'''

'''import turtle

def square_1():
 turtle.down()
 turtle.forward(100)
 turtle.left(90)
 turtle.forward(200)
 turtle.left(90)
 turtle.forward(200)
 turtle.left(90)
 turtle.forward(200)
 turtle.left(90)
 turtle.forward(100)

square_1()
turtle.right(90)
turtle.forward(10)
turtle.left(45)
square_1()
'''

'''import turtle


def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.pensize(3)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

size = 20
for i in range(5):
    drawSquare(alex, size)
    size = size + 20
    alex.penup()
    alex.goto(0, 0)
    alex.pendown()
    alex.pensize(3)

wn.exitonclick()'''

'''import turtle
#draw first circle
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(200)
#draw second circle
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.circle(150)
#draw third circle
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)
#draw fourth circle
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)
'''

'''from turtle import *

color('red', 'yellow')
begin_fill()
while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
end_fill()
done()'''