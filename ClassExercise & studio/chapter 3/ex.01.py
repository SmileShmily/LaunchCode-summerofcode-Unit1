'''Below is a short program that prompts the user to input the number of miles they are to drive on a given trip
and converts their answer to kilometers, printing the result. However, it doesn’t work properly.
 Find and fix the error in the program.
'''

miles = input("How many miles do you have to drive? ")
miles=float(miles)
kilometers = miles * 1.60934

print("That distance is equal to", kilometers, "kilometers")
