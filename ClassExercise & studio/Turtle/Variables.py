'''Additional notes

Something that confuses many beginners is the = symbol.
 In Math, whenever we see A = B, we know that A and B must be identical – in Math, = means “equality”.

However, = means something a little different in programming.
When we see A = B, it means that whatever A is will now be set equal to B – in programming, = means “assignment”.

So, if we see the following code:

my_variable = 3 + 4
print(my_variable)

my_variable = my_variable + 5
print(my_variable)

…the output will be 7 and 12.
We always computer whatever is on the right side, then change the variable on the left side to that value.'''

import turtle

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()