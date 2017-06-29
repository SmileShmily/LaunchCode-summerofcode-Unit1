
'''Chapter 8 Assignment
Write a function analyze_text that receives a string as input.
 Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text, a string like this:

"The text contains 243 alphabetic characters, of which 109 (44.8%) are ‘e’."'''
'''
#Debugging the code to see what happened

#the default str type
print(str, type(str))

#after the str is set as an argument
def analyze_text(str):
	# your code here
	print(str, type(str))

#after the str is used as input
str = "Eeeee"
print(str, type(str))

'''
'''def scrabble_score(word):
    word = word.lower()
    total = 0
    for i in word:
        if i in score:
            total = total + score[i]
    return total'''
'''
def scrabble_score(word):
    count = 0
    wordlist = list(word)
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerdic = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"} # dictionary for replacing upper case letters
    for letter in wordlist: # loop for getting rid of upper case letters
        if letter in capitals:
            wordlist.remove(letter)
            wordlist.append(lowerdic[letter])
    for item in wordlist: # scoring loopo
        count += score[item]
        return count

        '''
'''
def analyze_text(str):
    # your code here
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in str:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1


    percent_with_e = (numberOfe/totalChars) * 100
    print("The text contains", totalChars, "alphabetic characters, of which", numberOfe, "(", percent_with_e, "%)",
          "are 'e'.")
str1 ="Eeeee"
str2="Blueberries are tastee!"
str3="Wright's book, Gadsby, contains a total of 0 of that most common symbol;"
str4="Werewolf bar mitzvah, spooky! scary! Boys becoing men... men becoming wolves."


analyze_text(str1)
analyze_text(str2)
analyze_text(str3)
analyze_text(str4)

'''
'''
def analyze_text(str):
    # your code here
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in str:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1


    percent_with_e = (numberOfe/totalChars) * 100
    return ("The text contains",totalChars, "alphabetic characters, of which",numberOfe,"(", percent_with_e,"%)","are 'e'.")
str=input("Please enter a list of strings: ")
analyze_text(str)
'''
'''
def analyze_text(str):
    # your code here
    lows="abcdefghijklmnopqrstuvwxyz"
    ups="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in str:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1


    percent_with_e = (numberOfe/totalChars) * 100
   #return("The text contains %d alphabetic characters, of which %d (%.1f%) %sare 'e'."% (totalChars, numberOfe, percent_with_e))
    return totalChars,  numberOfe, percent_with_e
   # return ("The text contains",totalChars, "alphabetic characters, of which",numberOfe,"(", percent_with_e,"%)","are 'e'.")
str1 ="Eeeee"
str2="Blueberries are tastee!"
str3="Wright's book, Gadsby, contains a total of 0 of that most common symbol;"
str4="Werewolf bar mitzvah, spooky! scary! Boys becoing men... men becoming wolves."


print(analyze_text(str1))
print(analyze_text(str2))
print(analyze_text(str3))
print(analyze_text(str4))
'''

#str = input("Please enter your string：")
def analyze_text(str):
    # your code here
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

'''0 Your code failed the following tests:
    ---------------------------------------
    Your program crashed when I tried to run analyze_text with this string: 'Eeeee'
    The error is:
    not enough arguments for format string'''