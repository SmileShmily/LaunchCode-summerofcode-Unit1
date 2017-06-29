import sys


# Encrypt Plain Text
def caesar(plainText, key=0):
    cipherText = ""
    for c in plainText:
        if c.isalpha():
            if c.isupper():
                caps = True
            else:
                caps = False
            alphabet = ord(c.lower()) + key
            if alphabet > ord('z'):
                alphabet -= 26
            letter = chr(alphabet)
            if caps is True:
                letter = letter.upper()
            cipherText += letter
        else:
            cipherText += c
    return cipherText


# Brute force all 26 possibilities.
def guess_caesar(plainText):
    print('Showing all combinations for text ' + plainText)
    key = 1
    for c in range(0, 26):
        cipherText = caesar(plainText, key)
        print('Key ' + str(key) + ' => ' + cipherText)
        key += 1


# Main Program

# Usage
if len(sys.argv) == 1:
    print('\nCaesar Cypher Tool')
    print('\n Usage: ' + sys.argv[0] + ' (options) <text> <rot key>')
    print('\t encrypt         => \"Text to encrypt\" <key>')
    print('\t decrypt         => -d \"Text to decrypt\" <key>')
    print('\t decrypt file    => -f <filename> <key>')
    print('\t brute force     => -b \"Cyphertext\" \n')
# Brute force
elif sys.argv[1] == '-b':
    plainText = sys.argv[2]
    cipherText = guess_caesar(plainText)
    print(cipherText)
# Decode a string
elif sys.argv[1] == '-d':
    plainText = sys.argv[2]
    key = int(sys.argv[3])
    cipherText = caesar(plainText, key)
    print(cipherText)
# Decode a File
elif sys.argv[1] == '-f':
    infile = sys.argv[2]
    key = int(sys.argv[3])
    with open(infile, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(caesar(line, key))
# Encode a String
else:
    plainText = str(sys.argv[1])
    key = int(sys.argv[2])
    cipherText = caesar(plainText, key)
    print('\nEncrypting \"' + plainText + '\" with ROT' + str(key) + " => " + cipherText + '\n\n')