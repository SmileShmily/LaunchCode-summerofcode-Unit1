'''Write a program that will convert degrees fahrenheit to degrees celsius, like this:

What is the temperature in Farenheit?
#>>> 32
32.0 degrees Farenheit is 0.0 degrees Celsius.

'''

deg_f = int(input("What is the temperature in Farenheit? "))


deg_c = (deg_f- 32) / (5/ 9)

print(deg_f, " degrees Farenheit is", deg_c, " degrees Celsius.")

