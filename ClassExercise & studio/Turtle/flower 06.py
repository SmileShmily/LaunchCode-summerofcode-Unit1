import turtle

def drawSquare( size, pos ):
        #initialize position
        turtle.up()
        turtle.setpos(pos)
        turtle.down()
        # for loops iterate in this case from the first value until < 4, so
        for i in range (0,4):
                turtle.forward(size)
                turtle.right(90)
# Speeds up the turtle
turtle.speed(0)

# Format of a for loop
for i in range (0, 40):
        drawSquare( 10, (-400 + i * 20, 0))


# The equivalent loop using a while
i = 0
turtle.color("Blue")
while i < 40 :
        drawSquare( 10, (-400 + i * 20, 20 ))
        i = i + 1

turtle.exitonclick()