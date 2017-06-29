'''        ‘pineapple’ < ‘Peach’ = False

    (GRADED) Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a poem,
     a speech, instructions to bake a cake, some inspirational verses, etc.

Write a function that counts the number of alphabetic characters (a through z, or A through Z)
 in your text and then keeps track of how many are the letter ‘e’.
  Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.

'''

text = ''' "If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely'''
lowercase_text = text.lower()

def charCounter(some_text):
    e_counter = 0
    char_counter = 0

    for char in lowercase_text:
        if char == 'e':
            e_counter = e_counter + 1
        else:
            char_counter = char_counter + 1

    return ("Your text contains " + str(char_counter) +  " alphabetic characters, of which " + str(e_counter) + " (" + str((e_counter / char_counter) * 100) + "%)" +  "are 'e'.")

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
