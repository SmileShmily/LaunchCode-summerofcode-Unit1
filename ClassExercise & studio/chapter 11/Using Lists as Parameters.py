'''Functions which take lists as arguments and change them during execution are called modifiers and the changes they make are called side effects.
 Passing a list as an argument actually passes a reference to the list, not a copy of the list. Since lists are mutable,
  changes made to the elements referenced by the parameter change the same list that the argument is referencing.
   For example, the function below takes a list as an argument and multiplies each element in the list by 2:
'''
def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)
