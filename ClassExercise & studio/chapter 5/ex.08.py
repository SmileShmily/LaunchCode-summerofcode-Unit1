'''Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.
../_images/star1.png '''
import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wolfram = turtle.Turtle()
drawFivePointStar(wolfram)
