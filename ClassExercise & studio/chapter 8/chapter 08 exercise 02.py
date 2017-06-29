'''Write a function that counts the number of alphabetic characters (a thru z, or A thru Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'."'''

text = ''' "If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely'''

lowercase_text = text.lower()

def charCounter(some_text):
    e_counter = 0
    char_counter = 0

    '''for char in lowercase_text:
        if char == 'e':
            e_counter = e_counter + 1
        else:
            char_counter = char_counter + 1'''
    for char in lowercase_text:
        # Check if we have an alphanumeric string and continue the loop if not
        if not char.isalpha():
            continue
        # Increment the total character counter
        char_counter += 1
        # Additionaly, increment the 'e' counter if we have an 'e'
        if char == 'e':
            e_counter += 1

    return ("Your text contains " + str(char_counter) +  " alphabetic characters, of which " + str(e_counter) + " (" + str((e_counter / char_counter) * 100) + "%)" +  "are 'e'.")

print(charCounter(text))