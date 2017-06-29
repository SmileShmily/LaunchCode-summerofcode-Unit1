'''Create a turtle and assign it to a variable. When you print its type, what do you get?
'''

import turtle

tanenbaum = turtle.Turtle()

tanenbaum.color("blue")
tanenbaum.shape("turtle")


for i in range(1,100,5):
    tanenbaum.forward(i)
    tanenbaum.right(90)
    tanenbaum.stamp()
