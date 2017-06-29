'''You’ve written a program to convert degrees celsius to degrees fahrenheit.
The program below makes the conversion in the opposite direction, from fahrenheit to celsius.
However, it doesn’t work properly. Find and fix the error in the program.
'''

currentTemp_string = input("Enter a temperature in degrees fahrenheit: ")
currentTemp = int(currentTemp_string)

currentTempCelsius = (currentTemp - 32) * (5/9)
print("The temperature in Celsius is:", currentTempCelsius)
