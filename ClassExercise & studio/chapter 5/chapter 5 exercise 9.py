'''import turtle

def drawStar(t, n):
 for i in range(n):
      t.forward(100)
      t.left(180 - 180/n)

stroustrup = turtle.Turtle()
drawStar(stroustrup, 7)'''



import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

star = turtle.Turtle()
star.color('hotpink')
star.pensize(3)
star.fillcolor('hotpink')
star.speed(10)

def drawsStar(length, s):
    for i in range(5):
        s.forward(length)
        s.left(216)
def pattern(num_stars, s):
    for i in range(0, num_stars):
        drawsStar(100, s)
        s.right(360 / num_stars)
        s.penup()
        s.forward(100)
        s.pendown()


pattern(5, star)

'''
import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(30)
        t.left(216)
        t.color("hotpink")


wolfram = turtle.Turtle()
drawFivePointStar(wolfram)


wolfram.penup()
wolfram.forward(100)
wolfram.right(144)
wolfram.pendown()
wolfram.color("hotpink")
for i in range(5):
        wolfram.forward(30)
        wolfram.left(216)

'''
