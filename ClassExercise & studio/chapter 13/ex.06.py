'''Given three points that fall on the circumference of a circle, find the center and radius of the circle.
'''

def center_circle(p1, p2, p3):
    """Given three points that fall on the circumference of a circle, find the
    center and radius of the circle."""
    mr = (p2.y - p1.y) / (p2.x - p1.x)
    mt = (p3.y - p2.y) / (p3.x - p2.x)
    x = (mr*mt*(p3.y-p1.y)+mr*(p2.x+p3.x)-mt*(p1.x+p2.x))/(2*(mr-mt))
    y = -(1/mr)*(x-((p1.x+p2.x)/2))+(p1.y+p2.y)/2
    center = (x, y)
    radius = sqrt((p2.x-x)**2+(p2.y-y)**2)
    print ("center is: ", center)
    print ("radius is: ", radius)