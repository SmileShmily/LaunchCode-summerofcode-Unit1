'''The Ceasar cipher would be fairly easy to break. Let’s implement a more complicated cipher algorithm.

In a file vigenere.py, write a program that works similarly to caesar.py does above, but instead accepts a string at the command line that is used to encrypt the message. To see how the cipher should work, watch this short video on the Vigenere cipher courtesy of the CS50 folks at Harvard.

As you saw in the video, the Vigenere cipher uses a word as a key, rather than an integer.

Your program will work like this:

$ python3 vigenere.py launchcode
The crow flies at midnight!
Ehy ptvy tomps ug opfblkst!

Here, the user has entered “The crow flies at midnight” and the program printed “Ehy ptvy tomps ug opfblkst”.

By typing launchcode after our file name, that value is provided as a special type of input to our program, called a command line argument. We will have to do some extra work to use this value in our program, which is outlined outline below.
Reusing your Caesar code

You’ll find it very useful to have the functions alphabet_position and rotate_character from caesar.py, but rather than copy and paste them into vigenere.py let’s use a better approach.

You’ve imported modules such as math and random before. These modules were provided for you. It’s also possible (and quite useful!) to create and import your own modules.

Let’s import the functions we want to reuse from caesar.py. Put the following line at the top of vigenere.py.

from caesar import alphabet_position, rotate_character

This import syntax may be new to you. It says that we want to import code from a module caesar, but that we only want to import particular pieces of that module, in this case the functions alphabet_position and rotate_character. Since caesar.py is in the same directory as vigenere.py, the work required to import its code as a module is much simpler than you’ll usually encounter when using your own modules. You can read up on creating modules in Python in the Python module documentation.

Even though we only have one line of code (the import statement) in our file, let’s run it to make sure Python is able to find and import our Caesar code.

::
    $ python3 vigenere.py

Note: If you run vigenere.py at this point and see output, that means you left test code and print statements in caesar.py.
 Go back and clean them up, so only the 4 functions you were to have written remain.

Another note: If you receive an error when executing the file, make sure that you’re in the correct directory, and that both of your files are in that directory.
Getting the rotation key from the command line

In python, a list of the command-line arguments is made accessible to your program in the form of a list of strings: sys.argv.
 The first item, sys.argv[0] is always the name of your script, with the other arguments following. So, in our first example above where we ran

$ python3 vigenere.py launchcode

sys.argv would be ['vigenere.py', 'launchcode']. To use sys.argv, you need to add import sys to the top of your file.
You can read more about sys.argv in the official documentation.

With these details, you’re ready to tackle the program! Make sure your program behaves according to these details:
Specification

    You may assume that the command-line input consists only of alphabetic characters (no numbers, spaces, or symbols).
    If the user fails to enter a command-line parameter, you should print a helpful message and quit.
    Your program should preserve the case of each letter in the message string.
    You should only apply the cipher to a character that is a letter.
     When you encounter a symbol, space, or number in the string you are encoding you should simply leave it as-is.
      When this happens, you should remain at the same location in your key string for encoding the next character.
      For example, in the above example, here’s the way it should work.
      Notice how the cipher char progresses through the key string, and what happens when we encounter the space in the message string.

char from input string 	cipher char 	rotation amount 	result char
T 	l 	11 	E
h 	a 	0 	h
e 	u 	20 	y
(space) 	(space) 	n/a 	(space)
c 	n 	13 	p
r 	c 	2 	t
o 	h 	7 	v
w 	c 	2 	y
(and so on…)
Turn'''
'''
from string import ascii_uppercase as uc, ascii_lowercase as lc, maketrans

rotate = 13 # ROT13
rot = "".join([(x[:rotate][::-1] + x[rotate:][::-1])[::-1] for x in (uc,lc)])

def rot_func(text, encode=True):
    ascii = uc + lc
    src, trg = (ascii, rot) if encode else (rot, ascii)
    trans = maketrans(src, trg)
    return text.translate(trans)

text = "Text to ROT{}".format(rotate)
encode = rot_func(text)
decode = rot_func(encode, False)
'''
def rot13(s):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = chars[26:]+chars[:26]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    return ''.join(rot_char(c) for c in s)
print (rot13("Hello ,World!"))



import string

def rot(s, n=13):
    '''Encode string s with ROT-n, i.e., by shifting all letters n positions.
    When n is not supplied, ROT-13 encoding is assumed.
    '''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in s:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return(out)

def invrot(s, n=13):
    '''Decode a string s encoded with ROT-n-encoding
    When n is not supplied, ROT-13 is assumed.
    '''
    return(rot(s, -n))