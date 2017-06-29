'''
Donuts
'''

'''
Welcome to the Loop Hole!
Today's Manager's Special is:
Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Berries Oops All Berries
How many would you like?
>>> 3.33333
How much would you like to pay per donut (suggested price is $4.35 each)?
>>> 2.5
Ok, let me prepare that for you....
After tax, your total is: $8.74999125
Thank you for snacking! Loop back around here soon!

'''
print("Welcome to the Loop Hole!")

print("""Today's Manager's Special is:
Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Berries Oops All Berries""")

print("Ok, let me prepare that for you....")

num_donut=float(input("How many would you like?"))
print("You order number is:",num_donut,"pieces","\n")

cost_donut=float(input("How much would you like to pay per donut (suggested price is $4.35 each)?"))
print("The donut's price is:","$",cost_donut,"dollar","\n")

cost_total=round(num_donut*cost_donut,2)
print("You cost total is:","$",cost_total,"dollar","\n")

tax=0.05
pay_total=round(cost_total+cost_total*0.05,2)
print("After tax, your total is: ","$",pay_total,"dollar","\n")
print("Thank you for snacking! Loop back around here soon!")