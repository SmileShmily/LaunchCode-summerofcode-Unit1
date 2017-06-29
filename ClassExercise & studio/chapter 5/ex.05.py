'''Write a non-fruitful function drawEquitriangle(someturtle, somesize)
which calls drawPoly from the previous question to have its turtle draw a equilateral triangle.
'''
import turtle


def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(3):
        t.forward(sz)
        t.left(120)


def main():  # Define the main function
    wn = turtle.Screen()  # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()  # create alex
    drawSquare(alex, 100)  # Call the function to draw the square

    wn.exitonclick()


main()  # Invoke the main function