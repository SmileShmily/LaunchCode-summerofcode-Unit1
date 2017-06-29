from sys import argv
#print("I know that these are the words the user typed on the command line: ", argv)
from helpers import alphabet_position, rotate_character
'''
letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def alphabet_position(letter):
    rot = []
    for ch in letter:
        rot.append(ord(ch.upper()) - 65)
    return rot
def rotate_character(char, rot):
    ciphertext = ""
    for ch in char:
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + rot) % 26]
            else:
                ciphertext += letter_list[(ord(ch) - 97 + rot) % 26].lower()
        else:
            ciphertext += ch
    return ciphertext
    '''
'''
def rotate_character(char, rot, decode = False):
    if decode: rot= 26 - rot
    return "".join([chr((ord(i) - 65 + rot) % 26 + 65)
                for i in char.upper()
                if ord(i) >= 65 and ord(i) <= 90 ])
'''
def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        return False
    if (0 == int(cl_args[1].isdigit())):
        return False
    return True

def encrypt(text, rot):
    letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + rot) % 26]
            else:
                ciphertext += letter_list[(ord(ch) - 97 + rot) % 26].lower()
                # If the cipher text is not a letter, it is added directly to the cipher text string.
        else:
            ciphertext += ch
    return ciphertext

#print ("grandpa", user_input_is_valid("grandpa"))
#print ("5.0", user_input_is_valid(5.0))
#print ("5", user_input_is_valid(5))
'''
key="grandpa"
print(key.isdigit())
key="5.0"
print(key.isdigit())
key="5"
print(key.isdigit())
'''
'''
key = input("Rotate by:")
while (0 == int(key.isdigit())):  # 输入合法性判断
    print("Enter wrong,must int,please enter again:")
    key = input()
plaintext = input("Type a message:")
ciphertext = rotate_character(plaintext, int(key))
print("ciphertext:\n%s" % ciphertext)

user_input_is_valid = input("Rotate by:")
while (0 == int(user_input_is_valid.isdigit())):  # 输入合法性判断
    print("Enter wrong,must int,please enter again:")
    user_input_is_valid = input()
plaintext = input("Type a message:")
ciphertext = rotate_character(plaintext, int(user_input_is_valid))
print("ciphertext:\n%s" % ciphertext)'''
'''I know that these are the words the user typed on the command line:  ['E:/00.Python homework 6-13-2016/00.vocareum-- homework/Problem Set-----Crypto 00/caesar.py']
grandpa False
5.0 True
5 True
Rotate by:5.0
Enter wrong,must int,please enter again:
prandpa
Enter wrong,must int,please enter again:
5
Type a message:Hello,World!
ciphertext:
Mjqqt,Btwqi!
'''
