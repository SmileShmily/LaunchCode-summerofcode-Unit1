'''Functions can return tuples as return values.
 This is very useful — we often want to know some batsman’s highest and lowest score,
  or we want to find the mean and the standard deviation, or we want to know the year, the month,
   and the day, or if we’re doing some ecological modeling we may want to know the number of rabbits
   and the number of wolves on an island at a given time. In each case, a function (which can only return a single value),
   can create a single tuple holding multiple elements.

For example, we could write a function that returns both the area and the circumference of a circle of radius r.
'''

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))
