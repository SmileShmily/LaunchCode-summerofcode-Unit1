'''This will make a matrix of dots 5 dots wide and 7 dots high.
Try experimenting with the variables at the top to change the number of dots and the distance between them.

The for loop on the very inside (for i in range(width):) draws a single line of dots.
The code then causes the turtle to move back, then move down a row.'''
import turtle

seurat = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)

turtle.done()