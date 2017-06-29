'''Give the Python interpreter’s response to each of the following from a continuous interpreter session:

    #>>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
    #>>> d['banana']

   # >>> d['oranges'] = 20
   # >>> len(d)

    #>>> 'grapes' in d

   # >>> d['pears']

    #>>> d.get('pears', 0)

   # >>> fruits = d.keys()
    #>>> fruits.sort()
    #>>> print(fruits)

    #>>> del d['apples']
    #>>> 'apples' in d

Be sure you understand why you get each result. Then apply what you have learned to fill in the body of the function below:
'''

'''
def add_fruit(inventory, fruit, quantity=0):
    pass


# make these tests work...
Traceback(most
recent
call
last):
File
"<pyshell#1>", line
1, in < module >
d['banana']
KeyError: 'banana'
# new_inventory = {}
4
# add_fruit(new_inventory, 'strawberries', 10)
True
# test('strawberries' in new_inventory, True)
Traceback(most
recent
call
last):
File
"<pyshell#5>", line
1, in < module >
d['pears']
KeyError: 'pears'
# test(new_inventory['strawberries'], 10)
0
# add_fruit(new_inventory, 'strawberries', 25)
['apples', 'bananas', 'grapes', 'oranges']
# test(new_inventory['strawberries'] , 35)
False
'''

'''
def add_fruit(inventory, fruit, quantity=0):
    pass
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test('strawberries' in new_inventory, True)
test(new_inventory['strawberries'], 10)
add_fruit(new_inventory, 'strawberries', 25)
test(new_inventory['strawberries'] , 35)

'''

#def add_fruit(inventory, fruit, quantity=0):
  #           pass
def add_fruit(inventory, fruit, quantity=0):
        if fruit in inventory:
            inventory[fruit] += quantity
        else:
            inventory[fruit] = quantity
        print(inventory)
# make these tests work...

# new_inventory = {}

# add_fruit(new_inventory, 'strawberries', 10)

# test('strawberries' in new_inventory, True)

# test(new_inventory['strawberries'], 10)

# add_fruit(new_inventory, 'strawberries', 25)

# test(new_inventory['strawberries'] , 35)
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
assert ('strawberries' in new_inventory) == True
assert new_inventory['strawberries'] == 10
add_fruit(new_inventory, 'strawberries', 25)
assert new_inventory['strawberries'] == 35
