'''

(GRADED) This is a tricky one!

You have a thermostat that allows you to set the room to any temperature between 40 and 90 degrees.

The thermostat can be adjusted by turning a circular dial. If you turn the dial all the way to the left,
you will set the temperature to 40 degrees. If you turn to the right by one click, you will get 41 degrees.
As you continue to turn to the right, the temperature goes up, and the temperature gets closer and closer to 90 degrees.
 But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 and starts over.

Write a program that calculates the temperature based on how much the dial has been rotated.
You should prompt he user for a number of clicks-to-the-right. Then you should print the current temperature.

Here is an example of how your program should behave (When you see >>>, that line represents what the user is typing in):
By how many clicks has the dial been rotated?
#>>> 0
The temperature is 40

By how many clicks has the dial been rotated?
#>>> 24
The temperature is 64

By how many clicks has the dial been rotated?
#>>> 74
The temperature is 64

By how many clicks has the dial been rotated?
#>>> 49
The temperature is 89

By how many clicks has the dial been rotated?
#>>> 51
The temperature is 41

By how many clicks has the dial been rotated?
#>>> -1
The temperature is 89
'''

clicks_str = input("By how many clicks has the dial been turned?\n")
clicks = int(clicks_str)

# TODO calculate the temperature, and report it back to the user
current=(clicks%50+40)

print("The temperature is",current)