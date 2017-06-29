'''In chapter 9, you completed an exercise that had you write a function called rot13 that used Caesar’s cipher to encrypt a message.
 It encrypted a message by character by character, by rotating each letter 13 places to the right. It turned a into n, b into o, c into p and so on.
  It wrapped at the end of the alphabet, so that m shifted to z and then n shifted to a.
  Here’s the original problem statement, if you decided to skip that problem:

    Write a function called rot13 that uses the Caesar cipher to encrypt a message.
     The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to ‘its right’ in the alphabet.
     So for example the letter a becomes the letter n.
     If a letter is past the middle of the alphabet then the counting wraps around to the letter a again, so n becomes a, o becomes b and so on.
     Hint: Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic.

We’re going to build a more general version of this algorithm that allows a message to be encrypted using any rotation amount.
We’ll do this in a few steps, so you can break the problem down into isolate pieces.

alphabet_position

Open up a file caesar.py in your editor. Write a function alphabet_position(character) that takes a letter (that is, a string with only one alphabetic character) and returns the 0-based numerical position of that letter.
It should be case-insensitive.

Here are some example input parameter values, with the corresponding return values.
character 	Return value
a 	0
A 	0
b 	1
y 	24
z 	25
Z 	25

Don’t worry about what might happen if somebody tries to use your function with an input parameter that is something other than a single letter.

Test alphabet_position with various inputs before moving on to the next step. Use more tests than the examples we provide.

Recall that to run your program at the command line, you’ll need to type the following.
 Remember that $ signifies the command prompt in your terminal, whatever it may be.

$
rotate_string_13

Now, write a function rotate_string_13(text) that takes a word – that is, a string containing only letters (no spaces, numbers, or symbols) – as input and returns the result of rotating each letter in the string 13 places to the right. It should preserve the case of each letter.

Here are some example input values, with the corresponding return values.
text 	Return value
a 	n
abcd 	nopq
LaunchCode 	YnhapuPbqr

Test rotate_string_13 with various input values before moving on to the next stage. Use more tests than the examples we provide.

rotate_character

Write a function rotate_character(char, rot) that has as inputs a character char (that is, a string that consists of only a single letter) and an integer rot.
 It should return the result of rotating the character rot number of places to the right, preserving the case of the character.

Here are some example input values, with the corresponding return values.
char 	rot 	Return value
a 	13 	n
a 	14 	o
a 	0 	a
A 	13 	N
z 	1 	a
z 	2 	b
Z 	37 	k

Test rotate_character with various input values before moving on to the next stage. Use more tests than the examples we provide.

rotate_string

Write a function rotate_string(text, rot) that has as input a string and an integer, and returns the result of rotating each letter in the string rot places to the right.
The string may contain non-alphabetic characters (spaces, numbers, symbols). It should leave these as they are.

Here are some example input values, with the corresponding return values.
text 	rot 	Return value
a 	13 	n
abcd 	13 	nopq
LaunchCode 	13 	YnhapuPbqr
LaunchCode 	1 	MbvodiDpef
Hello, World! 	5 	Mjqqt, Btwqi!
V'''

def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )
s1="a"
s2="abcd"
s3="LaunchCode"
print(rot13(s1))
print(rot13(s2))
print(rot13(s3))

def caesar(s, k, decode = False):
    if decode: k = 26 - k
    return "".join([chr((ord(i) - 65 + k) % 26 + 65)
                for i in s.upper()
                if ord(i) >= 65 and ord(i) <= 90 ])

msg = "The quick brown fox jumped over the lazy dogs"
msg1="LaunchCode"
msg2="Hello, World!"
print (msg)
enc1 = caesar(msg1, 1)
enc2 = caesar(msg2, 5)
print (enc1)
print (enc2)
#print (caesar(enc, 11, decode = True))

