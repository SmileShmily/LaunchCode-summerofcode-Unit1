'''
monty = True
python = 1.234
monty_python = python ** 2
print(monty_python)

my_dict = {
    "name": "Arthur",
    "age": 24,
    "color":"blue",
    "game":"PoE"
}
print (my_dict.keys())
print (my_dict.values())
*************************************************************************************

my_dict = { "name": "Arthur", "age": 24, "color":"blue", "game":"PoE"}
print (my_dict.keys())
print (my_dict.values())

for key in my_dict:
    print (key, my_dict[key])

*************************************************************************************

my_dict = {
    "name": "Arthur",
    "age": 24,
    "color":"blue",
    "game":"PoE"
}
print (my_dict.items())
*************************************************************************************

squares = [x**2 for x in range(1,11)]
print (filter (lambda x: 30 <= x <= 70 , squares))
*************************************************************************************
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(2,11) if x%2 == 0]

print (even_squares)

cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4 == 0]
print (cubes_by_four)
*************************************************************************************
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::10]
print (backwards_by_tens)
*************************************************************************************
to_21 = range(1,22)

odds = to_21[::2]

middle_third = to_21[7:14]

print (to_21)
print (odds)
print (middle_third)
*************************************************************************************

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2])

*************************************************************************************
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print (movies.items())

*************************************************************************************

threes_and_fives = [ x for x in range(1,16) if ((x%3==0) or (x%5==0))]
print (threes_and_fives)
*************************************************************************************
a = 0b10111011
mask = 0b100
print (bin(a | mask))
*************************************************************************************
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print ("Yep! I'm edible.")
        else:
            print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()


class Animal(object):
    def __init__(self, name):
        self.name = name
        pass

zebra = Animal("Jeffrey")
print (zebra.name)
*************************************************************************************
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3) == 180:
            return True
        else:
            return False

*************************************************************************************
print ("The value of pi is around " + str(3.14))


string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
*************************************************************************************
name =input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")

print ("Ah, so your name is %s, your quest is %s, " \
       "and your favorite color is %s." % (name, quest, color))
*************************************************************************************
my_string = 'admin'
print (len(my_string))
print (my_string.upper())


ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())

pi = 3.14
print (str(pi))
*************************************************************************************
fifth_letter = "MONTY"[4]

print (fifth_letter)


from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day


print (now.year)
print (now.month)
print (now.day)
*************************************************************************************
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print (bool_five)



# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = (10+17)>3**16
print (str(bool_two))

# 1**2 <= -1
bool_three = 1**2 <= -1
print (str(bool_three))

# 40 * 4 >= -4
bool_four = 40*4 >=-4
print (str(bool_four))

# 100 != 10**2
bool_five = 100 != 10**2
print (bool_five)

*************************************************************************************
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())
*************************************************************************************
def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()
clinic()
*************************************************************************************
def the_flying_circus():
    if True or True:    # Start coding here!
        return True # Don't forget to indent
        # the code inside this block!
    elif 7 >= 2:
        return 'nooo' # Keep going here.
        # You'll want to add the else statement, too!
    else:
        return 'non'

print(the_flying_circus())

*************************************************************************************
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input('TELL ME a word in ENGRIXH:').lower()
if len(original) > 0 and original.isalpha():
    print (original.lower())
else:
    print ('empty')
*************************************************************************************

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]

    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')
*************************************************************************************
def biggest_number(*args):
    print (max(args))
    return max(args)

def smallest_number(*args):
    print (min(args))
    return min(args)

def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
*************************************************************************************

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print ("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

*************************************************************************************
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print ("%d squared is %d." % (n, squared))
    return squared

# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)
*************************************************************************************
def cube(number):
    raw = number **3
    return raw

def by_three(number):
    if number % 3 == 0:
        number = number **3
        print (number)
        return number
    else:
        print ('n isnt')
        return False


*************************************************************************************


import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print (everything)       # Prints 'em all!
*************************************************************************************
import math
print (math.sqrt(25))

*************************************************************************************

def shut_down(s):
    if s == "yes":
        return 'Shutting down'
    elif s == "no":
        return 'Shutdown aborted'
    else:
        return 'Sorry'
print(shut_down("yes"))
*************************************************************************************
def hotel_cost(nights):
    return nights*140
    print (nights*140)

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
print (plane_ride_cost('Charlotte'))
*************************************************************************************

def hotel_cost(nights):
    return nights*140
    print (nights*140)

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475

def rental_car_cost(days):
    total = days*40
    if days >= 7:
        tuto = total - 50
        return tuto
    elif days >= 3 and days < 7:
        tato = total - 20
        return tato
    else:
        total = days*40
        return total

def trip_cost(city, days, spending_money):
    notreal = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return notreal

print (trip_cost("Los Angeles", 5, 600))
'''