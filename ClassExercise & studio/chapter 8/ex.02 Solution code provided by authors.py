'''Write a function that counts the number of alphabetic characters (a thru z, or A thru Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'."'''

def count(p):
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1


    percent_with_e = (numberOfe/totalChars) * 100
    print("Your text contains", totalChars, "alphabetic characters of which", numberOfe, "(", percent_with_e, "%)", "are 'e'.")


p = '''"If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely'''

count(p)


def analyze_text(str):
    # your code here


# Don't copy these tests into Vocareum
from test import testEqual

str = "Eeeee"
expected = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(str), expected)

str = "Blueberries are tastee!"
expected = "The text contains 20 alphabetic characters, of which 6 (30.0%) are 'e'."
testEqual(analyze_text(str), expected)

str = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
expected = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(str), expected)
