import turtle
screen=turtle.Screen()
t=turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.stamp()
move=30
for i in range(12):
        t.penup()
        t.forward(50)
        t.pendown()
        t.penup()
        t.forward(15)
        t.stamp()
        t.home()
        t.right(move)
        move=move+30