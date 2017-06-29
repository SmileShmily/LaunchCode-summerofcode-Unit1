'''Using the turtle graphics module, write a recursive program to display a Hilbert curve.
'''
import turtle
import random
import timeit
import os
import os.path
basicpoints = [(20, 80), (80, 80), (20, 80), (80, 80)]
def drawZ(level, pos):
    points = []
    if pos == 0:
        pass
    elif pos == 1:
        pass
    elif pos == 2:
        points = basicpoints
    elif pos == 3:
        pass

def drawHilbert(level):
    if level == 1:
        for i in range(0, 4):
            drawZ(1, i)
    else:
        for i in range(0, 4):
            drawHilbert(level - 1)