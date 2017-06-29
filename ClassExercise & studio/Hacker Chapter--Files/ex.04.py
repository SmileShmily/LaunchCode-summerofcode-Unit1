'''Here is a file called labdata.txt that contains some sample data from a lab experiment.

44 71
79 37
78 24
41 76
19 12
19 32
28 36
22 58
89 92
91 6
53 7
27 80
14 34
8 81
80 19
46 72
83 96
88 18
96 48
77 67

Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair.
 Write a function called plotRegression that reads the data from this file and uses a turtle to plot those points and a best fit line according to the following formulas:

y=y¯+m(x−x¯)

m=∑xiyi−nx¯y¯∑x2i−nx¯2

where x¯
is the mean of the x-values, y¯ is the mean of the y- values and n is the number of points.
If you are not familiar with the mathematical ∑ it is the sum operation. For example

∑xi means to add up all the x values.

Your program should analyze the points and correctly scale the window using setworldcoordinates so that that each point can be plotted.
 Then you should draw the best fit line, in a different color, through the points.
'''

'''
def plot(data):
    import turtle

    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    # Set up our variables for the formula.
    x_lst, y_lst = [i[0] for i in data], [i[1] for i in data]
    x_sum, y_sum = float(sum(x_lst)), float(sum(y_lst))
    x_mean, y_mean = x_sum / len(x_lst), y_sum / len(y_lst)

    # Not sure about the formula where x and E are concerned ...
    m = ((x_sum * y_sum) - (20 * x_mean * y_mean)) / (x_sum ** 2 - (20 * x_mean ** 2))
    y = y_mean + m * (x_sum - x_mean)  # This gives 966=x_sum so it can't be right.

    # Get min and max values for coordinate system.
    x_min, x_max, y_min, y_max = min(x_lst), max(x_lst), min(y_lst), max(y_lst)
    # Add 10 points on each line to be safe.
    wn.setworldcoordinates(x_min - 10, y_min - 10, x_max + 10, y_max + 10)

    for i in data:
        t.setpos(i[0], i[1])

    wn.exitonclick()


with open("lib/labdata.txt") as f:
    coords = [map(int, line.split()) for line in f]

plot(coords)
'''


def plot(data):
    import turtle

    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    # Set up our variables for the formula.
    x_lst, y_lst = [i[0] for i in data], [i[1] for i in data]
    x_sum, y_sum = float(sum(x_lst)), float(sum(y_lst))
    x_mean, y_mean = x_sum / len(x_lst), y_sum / len(y_lst)

    # Not sure about the formula where x and E are concerned ...
    m = ((x_sum * y_sum) - (20 * x_mean * y_mean)) / (x_sum ** 2 - (20 * x_mean ** 2))
    y = y_mean + m * (x_sum - x_mean)  # This gives 966=x_sum so it can't be right.

    # Get min and max values for coordinate system.
    x_min, x_max, y_min, y_max = min(x_lst), max(x_lst), min(y_lst), max(y_lst)
    # Add 10 points on each line to be safe.
    wn.setworldcoordinates(x_min - 10, y_min - 10, x_max + 10, y_max + 10)

    for i in data:
        t.setpos(i[0], i[1])

    wn.exitonclick()


f = open("studentdata.txt", "r")

coords = [map(int, line.split()) for line in f]

plot(coords)
