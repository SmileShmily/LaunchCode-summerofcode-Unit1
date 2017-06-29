'''    ’

(GRADED) Write a function analyze_text that receives a string as input.
 Your function should count the number of alphabetic characters (a through z, or A through Z)
in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text, something like this:
 The text contains 243 alphabetic characters, of which 109 (44.8%) are ‘e’.

'''


#analyze_text=input("Please enter your str:")
def analyze_text(str):
    # your code here
#  lows="abcdefghijklmnopqrstuvwxyz"
#  ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str = repr(str).lower()
    numberOfe = 0
    totalChars = 0
    for ch in str:
         if ((ch <= 'Z' and ch >= 'A') or (ch <= 'z' and ch >= 'a')):
            totalChars = totalChars + 1
            if ch == 'e':
                numberOfe = numberOfe + 1
    percent_with_e = (numberOfe/totalChars) * 100
    return("The text contains %d alphabetic characters, of which %d (%.1f%) %sare 'e'."% (totalChars, numberOfe, percent_with_e))

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
'''Output

Pass
Pass
Pass'''