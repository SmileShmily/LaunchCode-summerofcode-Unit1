'''Additional notes

Why did I pick the number “144”? Why is that significant? What happens if you try changing a different number?'''

import turtle

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)

turtle.done()