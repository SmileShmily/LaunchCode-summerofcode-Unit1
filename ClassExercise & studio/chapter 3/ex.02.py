'''Picture a compass where north represents 0 degrees, east represents, 90 degrees, and so on,
all the way around to 360 degrees, which is again the same as 0 degrees: true north.

The program below envisions the scenario in which a person is facing north (aka 0 degrees)
and spins some number of rotations, either clockwise or counter-clockwise (-1 represents a full counter-clockwise spin,
 1 a full clockwise spin). It calculates the direction they end up facing in degrees. However, it doesn’t work properly.
  Find and fix the error in the program.
'''

spins = input("How many times did you spin? (Enter a negative number for couter-clockwise spins) ")

degrees = float(spins) %360

print("You are facing", degrees, "degrees relative to north")
