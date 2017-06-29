
'''At the end of ActiveCode 1 you will notice that we call the function myWin.exitonclick(),
this is a handy little method of the window that puts the turtle into a wait mode until you click inside the window,
after which the program cleans up and exits.'''
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()
