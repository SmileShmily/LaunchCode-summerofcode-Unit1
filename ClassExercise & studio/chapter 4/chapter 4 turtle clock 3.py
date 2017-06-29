import turtle  # set up alex

wn = turtle.Screen()
wn.bgcolor("SpringGreen")

hyoun = turtle.Turtle()
hyoun.color("Blue")
hyoun.shape("turtle")

for tick in range(12):
    hyoun.up()
    hyoun.forward(80)
    hyoun.down()
    hyoun.forward(10)
    hyoun.up()
    hyoun.forward(30)
    hyoun.stamp()
    hyoun.backward(120)
    hyoun.left(30)

hyoun.stamp()