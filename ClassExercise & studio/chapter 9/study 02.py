'''Optional parameters

To find the locations of the second or third occurrence of a character in a string, we can modify the find function,
 adding a third parameter for the starting position in the search string:
'''

def find2(astring, achar, start):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find2('banana', 'a', 2))