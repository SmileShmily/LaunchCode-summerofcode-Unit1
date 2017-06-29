
'''Draw this pretty pattern.
../_images/tess08.png '''
'''
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

brandon = turtle.Turtle()
brandon.fillcolor('blue')
brandon.pencolor('blue')
brandon.pensize(3)


def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,180):
    brandon.left(360/i)
    drawsq(brandon, 50)
'''
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

brandon = turtle.Turtle()
brandon.fillcolor('blue')
brandon.pencolor('blue')
brandon.pensize(3)

brandon.down
brandon.speed(0)


def drawsq(length, s):
    for i in range(4):
        s.forward(length)
        s.left(90)
#s=my square

def pattern(num_squares, s):
    for i in range(0, num_squares):
        drawsq(100, s)
        s.right(360 / num_squares)


pattern(80, brandon)

