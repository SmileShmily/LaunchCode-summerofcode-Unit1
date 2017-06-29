'''Modify the recursive tree program using one or all of the following ideas:

    Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
    Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
    Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range.
    For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
    Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

If you implement all of the above ideas you will have a very realistic looking tree.
'''
import turtle
import random
#import timeit
#import os
#import os.path
def tree(branchLen, t):
    if branchLen > 5:
        oldwidth = t.width()
        t.width(oldwidth - 2.5)
        t.forward(branchLen)
        angle = random.randint(15, 45)
        subtract = random.randint(5, 20)
        t.right(angle)
        tree(branchLen - subtract, t)
        t.left(angle * 2)
        tree(branchLen - subtract, t)
        t.right(angle)
        t.backward(branchLen)
        t.width(oldwidth)

def drawtree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.width(20)
    tree(75,t)
    myWin.exitonclick()
drawtree()