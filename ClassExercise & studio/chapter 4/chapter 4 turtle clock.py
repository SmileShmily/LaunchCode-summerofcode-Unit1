import turtle
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
#clr=['red','green','blue','yellow','purple']
trtl.pensize(4)
n=0
trtl.shape('turtle')
trtl.penup()
trtl.pencolor('red')
for m in range(12):
    m=m+1
    trtl.penup()
    trtl.forward(150)
    trtl.pendown()
    trtl.forward(25)
    trtl.penup()
    trtl.forward(20)
    trtl.write(m,align="center",font=("Arial", 12, "normal"))
    #if m == 12:m = 0
    trtl.home()
    trtl.right(n)
    n = n + 30
trtl.home()
trtl.setpos(0,-250)
trtl.pendown()
trtl.pensize(10)
trtl.pencolor('blue')
trtl.circle(250)
trtl.penup()
trtl.setpos(150,-270)
trtl.pendown()
#trtl.pencolor('pink')
#trtl.write('Shmily',font=("Arial", 12, "normal"))
#trtl.ht()