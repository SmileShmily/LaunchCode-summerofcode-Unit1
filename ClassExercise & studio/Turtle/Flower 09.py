import turtle

turtle.hideturtle()
turtle.speed('fastest')
turtle.tracer(False)

def petal(radius,steps):
    turtle.circle(radius,90,steps)
    turtle.left(90)
    turtle.circle(radius,90,steps)

num_petals = 8
steps = 8
radius = 100

for i in range(num_petals):
    turtle.setheading(0)
    turtle.right(360*i/num_petals)
    petal(radius,steps)

turtle.tracer(True)
turtle.done()
