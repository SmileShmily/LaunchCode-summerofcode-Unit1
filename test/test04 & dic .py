'''
people = 30
cars = 40
buses = 15
if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")
*************************************************************************************
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print (residents['Sloth'])
print (residents['Burmese Python'])
*************************************************************************************
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 2

print (zoo_animals)


backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print (backpack)
*************************************************************************************
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['pocket'].sort()
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['backpack'].sort()
inventory['gold'] = inventory['gold'] +50
*************************************************************************************
zoo_animals = ["pangolin", "cassowary", "sloth", "cat"];
# One animal is missing!

if len(zoo_animals) > 3:
	print ("The first animal at the zoo is the " + zoo_animals[0])
	print ("The second animal at the zoo is the " + zoo_animals[1])
	print ("The third animal at the zoo is the " + zoo_animals[2])
	print ("The fourth animal at the zoo is the " + zoo_animals[3])

*************************************************************************************

numbers = [5, 6, 7, 8]

print ("Adding the numbers at indices 0 and 2...")
print (numbers[0] + numbers[2])
print ("Adding the numbers at indices 1 and 3...")
# Your code here!
print (numbers[1] + numbers[3])

*************************************************************************************

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
print (first)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
print (middle)
last   = suitcase[4:6]  # The last two items (index four and five)
print (last)
*************************************************************************************
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index('duck')   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, 'cobra')


print (animals) # Observe what prints after the insert operation

*************************************************************************************


my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print (2*number)

*************************************************************************************


start_list = [5, 3, 1, 2, 4]
square_list = []

# for loop number is ambiguous variable

for number in start_list:
    square = number ** 2 # calculate square to add later
    square_list.append(square) # add the calculation
    square_list.sort()
print (square_list) # print sorted version

*************************************************************************************

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print (webster[key])

*************************************************************************************

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print (number)
*************************************************************************************
def fizz_count(x):
    count = 0
    for i in x:
        if (i == "fizz"):
            count = count  + 1
    return count
    print (count)

*************************************************************************************


for letter in "Codecademy":
    print (letter)
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print (letter)
********************************************************************************


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

for key in prices:
    print ("%s" %key)
    print ("price: %s" %prices[key])
    print ("stock: %s" %stock[key])

total = 0
for n in stock:
    total = total + (stock[n] * prices[n])
print (total)

*************************************************************************************
*************************************************************************************

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for n in food:
        if stock[n] > 0:
            total = total + prices[n]
            stock[n] -= 1
        else:
            total = total
    print (total)
    return total
#*************************************************************************************

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

print (lloyd["name"])
print (lloyd["homework"])
print (lloyd["quizzes"])
print (lloyd["tests"])

print (alice["name"])
print (alice["homework"])
print (alice["quizzes"])
print (alice["tests"])

print (tyler["name"])
print (tyler["homework"])
print (tyler["quizzes"])
print (tyler["tests"])

#*************************************************************************************

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total

def get_average(student):
    homework = average(student["homework"])* 0.1
    quizzes = average(student["quizzes"])* 0.3
    tests = average(student["tests"])* 0.6

    avrg = homework + quizzes + tests
    return avrg

def get_letter_grade(score):
    if score>= 90:
        return 'A'
    elif score>= 80:
        return 'B'
    elif score>= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

print (get_class_average(students))
print( get_letter_grade(get_class_average(students)))
#*******************************************************************************
number = 5
def my_function(x):
    return x * 3

print (my_function(number))
#*******************************************************************************


n = "Hello"
# Your function here!
def string_function(s):
    return s + 'world'
print (string_function(n))

#*******************************************************************************


n = [1, 3, 5]

# Add your code below
print (n[1])

#*******************************************************************************

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print (n)

#*******************************************************************************

n = [1, 3, 5]
# Removes 1 from the list,
# NOT the item at index 1
n.remove(1)
# Another possible solution, will remove the item at the given index:
del(n[0])
# Another possible solution will remove the item at index from the list and return it to you:
n.pop(0)
print (n)
#*******************************************************************************



word = "eggs!"

# Your code here!
for a in word:
    print (a)


#*******************************************************************************


numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
    print (num)

# Add your loop below!
for num in numbers:
    print (num ** 2)


#*******************************************************************************


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!') # (It actually is.)
        break
    print ('A', f)
else:
    print ('A fine selection of fruits!' )
#*******************************************************************************
'''

