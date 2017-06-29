import turtle
import random

win=turtle.Screen()
win.bgcolor("lightblue")
#create 2 turtle
zach=turtle.Turtle()
jesses=turtle.Turtle()
#speed them up
zach.speed(10)
jesses.speed(15)
zach.color("blue")
jesses.color("red")
#generate[0,2,4,6,8,....48]
for i in range(0,50,2):
 zach.penup()
 zach.forward(50)
 zach.left(90)
 zach.pendown()
 zach.penup()
 zach.forward(15)
 zach.stamp()


 jesses.penup()
 jesses.forward(50)
 jesses.left(90)
 jesses.pendown()
 jesses.penup()
 jesses.forward(15)
 jesses.stamp()
#distance is equal to something reasonable
zach_distance=-random.randrange(1,30)
jesses_distance=-random.randrange(1,30)


#creat a random angle for each turtle
zach_angle=random.randrange(0,181)
jesses_angle=random.randrange(0,181)

win.exitonclick()
