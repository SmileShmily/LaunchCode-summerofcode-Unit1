letter_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # int letter_list


# encrypt
def Encrypt(plaintext, key):
    ciphertext = ""
    for ch in plaintext:  # ergodic
        if ch.isalpha():  #  Whether the text is for the letter, if it is, then determine the size of the write, respectively, to encrypt
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + key) % 26]
            else:
                ciphertext += letter_list[(ord(ch) - 97 + key) % 26].lower()
        else:  # If the cipher text is not a letter, it is added directly to the cipher text string.
            ciphertext += ch
    return ciphertext


# decryption
def Decrypt(ciphertext, key):
    plaintext = ""
    for ch in ciphertext:  # Ergodic cipher
        if ch.isalpha():  # The cipher text is not for the letter, if it is, then the case is to determine the size of the write, respectively, to decrypt
            if ch.isupper():
                plaintext += letter_list[(ord(ch) - 65 - key) % 26]
            else:
                plaintext += letter_list[(ord(ch) - 97 - key) % 26].lower()
        else:  # If the cipher text is not a letter, it is added directly to the text string.
            plaintext += ch
    return plaintext


# main()
print("Encryption, please press D, decryption, please press E:")
user_input = input();
while (user_input != 'D' and user_input != 'E'):  #  Enter a valid judgment
    print("Enter a wrong! Please re-enter:")
    user_input = input()

print("Rotate by:")
key = input()
while (0 == int(key.isdigit())):  #  Enter a valid judgment
    print("Enter a wrong! The key is the letter. Please re-enter:")
    key = input()

if user_input == 'D':
    #encrypt
    print("Type a message:")
    plaintext = input()
    ciphertext = Encrypt(plaintext, int(key))
    print("ciphertext:\n%s" % ciphertext)
else:
    # Decrypt
    print("Please enter the cipher text:")
    ciphertext = input()
    plaintext = Decrypt(ciphertext, int(key))
    print("Plaintext:\n%s" % plaintext)