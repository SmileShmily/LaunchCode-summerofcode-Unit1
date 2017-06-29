from sys import argv
#print("I know that these are the words the user typed on the command line: ", argv)
from helpers import alphabet_position,encrypt
#letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
'''
letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alphabet_position(letter):
    rot = []
    for ch in letter:
        rot.append(ord(ch.upper()) - 65)
    return rot
    '''

def encrypt(text, rot):
    letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ""
    i = 0
    for ch in text:
        if 0 == i % len(rot):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + alphabet_position(rot[i])) % 26]
                i += 1
            else:
                ciphertext += letter_list[(ord(ch) - 97 + alphabet_position(rot[i])) % 26].lower()
                i += 1
        else:
            ciphertext += ch
    return ciphertext
'''
letter = input("Encryption key:")
rot = letter
text = input("Type a message:")
ciphertext = encrypt(text, rot)
print("ciphertext:\n%s" % ciphertext)
'''
'''I know that these are the words the user typed on the command line:  ['E:/00.Python homework 6-13-2016/00.vocareum-- homework/Problem Set-----Crypto 00/vigenere.py']
Encryption key:boom
Type a message:hello
ciphertext:
iszxp
'''