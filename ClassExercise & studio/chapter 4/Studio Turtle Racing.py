'''
Turtle Races

In this studio we are going to work step by step through the problem of racing turtles.
The idea is that we want to create two or more turtles and have them race across the screen from left to right.
The turtle that goes the farthest is the winner.

There are several different, and equally plausible, solutions to this problem. Let’s look at what needs to be done,
and then look at some of the options for the solution. To start,
 let’s think about a solution to the simplest form of the problem, a race between two turtles.
  We’ll look at more complex races later.

When you are faced with a problem like this in computer science it is often a good idea to find a solution to a simple problem
first and then figure out how to make the solution more general.

Here is a possible sequence of steps that we will need to accomplish:

    Import the modules we need
    Create a screen
    Create two turtles
    Move the turtles to their starting positions
    Send them moving across the screen

Here is the Python code for the first 4 steps above
'''

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# your code goes here
#c = random.randrange(1,9)
for c in range(0,50,2):
    andy.color()
    andy.forward(c)
    andy.left(90)
    lance.color()
    lance.forward(c)
    lance.left(90)
wn.exitonclick()
