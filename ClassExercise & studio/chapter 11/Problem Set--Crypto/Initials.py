'''In a file initials.py, write a program that prompts the user to enter their full name at the command line, and then prints out their capitalized initials.
You may assume that the user’s input will contain only letters (uppercase and/or lowercase) plus single spaces between words.
 This means you don’t have to worry about Conan O’Brien, T.S. Eliot, or Cee-Lo Green.

Here are some example input/output pairs:
Input 	Output
Ozzie Smith 	OS
bonnie blair 	BB
George 	G
Daniel Day Lewis 	DDL

Your program should work like this:

$ python3 initials.py
Ozzie Smith
OS

Note that we’re not using a prompt string, but rather dumbly waiting for the user to type in the name.
Tips and hints

    Note that our output is on a single line. This means you’ll need to collect the initials

        as you find them, rather than printing each one out.
        This will look similar to the accumulator pattern that we discussed in Chapter 5, but with strings instead of integers.

    Remember that we’ve been using Python 3 in this class.
    If you use the input function with Python 2 – by calling python initials.py, for example – then you’ll run up against some unexpected behavior.

    When using input, to prompt without a messages you may either provide the empty string '' as the parameter,
    or call it without any parameters and python will use the empty string by default.

'''
myname=input("what's your name:")
#myname = "Edgar Allan Poe"
namelist = myname.split()
init = ""
for aname in namelist:
    init = init + aname[0]
print(init)