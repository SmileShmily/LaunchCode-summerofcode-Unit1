import turtle

def side(size,level):
        if (level == 0):
            t.forward(size)
            return
        side(size/3,level-1)
        t.left(60)
        side(size/3,level-1)
        t.right(120)
        side(size/3,level-1)
        t.left(60)
        side(size/3,level-1)

def snowflake(size,level):
        for i in (1,3):
            side(size,level)
            t.right(120)

t = turtle.Pen()
snowflake(250,4)