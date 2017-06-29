'''Instructions:

    "You forgot to give Professor Boolean's favorite rabbit specimen a name? You know how picky the professor is!
    Only particular names will do! Fix this immediately, before you're... eliminated!"

    Luckily, your minion friend has already come up with a list of possible names,
    and we all know that the professor has always had a thing for names with lots of letters near the 'tail end' of the alphabet,
    so to speak. You realize that if you assign the value 1 to the letter A, 2 to B, and so on up to 26 for Z,
    and add up the values for all of the letters, the names with the highest total values will be the professor's favorites.
    For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43, while the name Earz, though shorter, has value 5 + 1 + 18 + 26 = 50.

    If two names have the same value, Professor Boolean prefers the lexicographically larger name.
    For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

    Write a function answer(names) which takes a list of names and returns the list sorted in descending order of how much the professor likes them.

    There will be at least 1 and no more than 1000 names. Each name will consist only of lower case letters.
     The length of each name will be at least 1 and no more than 8.

    Test cases:

    Inputs:

    (string list) names = ["annie", "bonnie", "liz"]

    Output:

    (string list) ["bonnie", "liz", "annie"]

    Inputs:

    (string list) names = ["abcdefg", "vi"]

    Output:

    (string list) ["vi", "abcdefg"]

    Your code will run inside a Python 2.7.6 sandbox.

    Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.
'''

def answer(names):
    # Sort names by reverse alphebetical order
    names = sorted(names, reverse=True)
    # Evaluate the value of each name and build a list with name,value pairs
    name_with_values = sorted([((current_name,value(current_name))) for current_name in names],
        key=lambda value: value[1], reverse=True)
    # Return the list only containing the names
    return [name[0] for name in name_with_values]

def value(name):
    # Evaluate and return value of the name
    return sum([ord(letter) - 96 for letter in name])

print( answer(names = ["annie", "bonnie", "liz", "bpnnid"]))