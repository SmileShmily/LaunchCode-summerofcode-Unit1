#A simple example of recursion - using the Koch snowflake
# (in houdini it would be an L-system
# Premis is F++F++F (turtle defined triangle)
# Rules is F=F-F++F-F
# This is due to the fact the angle used is 60 so ++ is right(120)

import turtle

koch_flake = "FRFRF"
iterations = 3

for i in range(iterations):
    koch_flake = koch_flake.replace("F", "FLFRFLF")

turtle.down()

for move in koch_flake:
    if move == "F":
        turtle.forward(100.0 / (3 ** (iterations - 1)))
    elif move == "L":
        turtle.left(60)
    elif move == "R":
        turtle.right(120)