'''Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer, like this:

How many miles have you driven?
#>>> 150
How many gallons have you used?
#>>> 5
Your car gets 30 miles per gallon.

'''

driven = int(input("How many miles have you driven?"))
used= int(input("How many gallons have you used? "))
final=driven/used
print("Your car gets", final,"miles per gallon.")