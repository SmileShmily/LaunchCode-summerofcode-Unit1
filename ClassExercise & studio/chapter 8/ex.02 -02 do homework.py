'''Write a function that counts the number of alphabetic characters (a thru z, or A thru Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'."'''

#quote = '''Cine e cu noi? cine e impotriva noastra? Noi suntem singurii care putem decide asta'''
'''
def count(text,letter):
    total_text = 0
    total_letter = 0
    for a in text:
         if ord(a.lower()) in range (97,123):
               total_text = total_text + 1
               if ord(a.lower()) == ord(letter.lower()):
                    total_letter = total_letter + 1
print("Your text contains ", total_text, " alphabetic characters, of which ", total_letter,"(",round(total_letter / total_text *100,1),"%) are '",letter,"'.")
count(quote,"e")
'''

def analyze_text(str):
    # your code here
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for ch in str:
        if ch in lows or ch in ups:
            totalChars = totalChars + 1
            if ch == 'e':
                numberOfe = numberOfe + 1
    percent_with_e = (numberOfe/totalChars) * 100
    return "The text contains",totalChars, "alphabetic characters, of which",numberOfe,"(", percent_with_e,"%)","are 'e'."

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
