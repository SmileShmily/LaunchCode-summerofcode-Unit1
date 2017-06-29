'''Modify the walking turtle program so that rather than a 90 degree left or right turn the angle of the turn is determined randomly at each step.

'''


def wandering_turtle():
    """Modify the walking turtle program so that rather than a 90 degree left or
    right turn the angle of the turn is determined randomly at each step.
    Modify the turtle walk program so that you have two turtles each with a random
    starting location. Keep the turtles moving until one of them leaves the screen.
    Modify the previous turtle walk program so that the turtle turns around when
    it hits the wall or when one turtle collides with another turtle."""
    u = turtle.Turtle()
    u.shape("turtle")
    u.color("green")
    t.color("red")
    for i in [t, u]:
        i.penup()
        i.setpos(random.randrange(-300, 300), random.randrange(-300, 300))
        i.pendown()

    while True:
        for t1, t2 in [(t, u), (u, t)]:
            coin = random.randrange(2)
            angle = random.randrange(360)
            if coin:
                t1.left(angle)
            else:
                t1.right(angle)
            t1.forward(50)
            if t1.distance(0, 0) > 390 or t1.distance(t2) < 25:
                t1.setpow(0, 0)
        return wandering_turtle()