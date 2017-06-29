
'''
import string
str=input("Please enter your str:")

def analyze_text(str,char):
    total_str = 0
    total_char = 0
    for a in str:
          if ord(a.lower()) in range (97,123):
              total_str = total_str + 1
          if ord(a.lower()) == ord(letter.lower()):
              total_char = total_char + 1
print("Your text contains ", total_str, " alphabetic characters, of which ", total_char,"(",round(total_char / total_str *100,1),"%) are '",char,"'.")
str.count(str,"e")
'''
#analyze_text=input("Please enter your str:")
def analyze_text(str):
    # your code here
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for ch in str:
        #if ((ch <= 'Z' and ch >= 'A') or (ch <= 'z' and ch >= 'a')):
        if ch in lows or ch in ups:
            totalChars = totalChars + 1
            if ch == 'e':
                numberOfe = numberOfe + 1
    percent_with_e = (numberOfe/totalChars) * 100
    return ("The text contains %d alphabetic characters, of which %d (%.1f%)  are 'e'." % (totalChars, numberOfe, percent_with_e))


'''
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
testEqual(analyze_text(str), expected)'''

