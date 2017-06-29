
'''

The keys method returns what Python 3 calls a view of its underlying keys.
We can iterate over the view or turn the view into a list by using the list conversion function.
'''
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)




inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)





inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
    print('apples' in inventory)
    print('cherries' in inventory)

    if 'bananas' in inventory:
        print(inventory['bananas'])
    else:
        print("We have no bananas")





inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))




mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
keylist = list(mydict.keys())
keylist.sort()
print(keylist[3])
'''Correct! Yes, the list of keys is sorted and the item at index 3 is printed.'''



