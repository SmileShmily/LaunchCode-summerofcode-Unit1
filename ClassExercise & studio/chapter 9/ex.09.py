'''Write a function that decrypts the message from the previous exercise. It should also take two parameters. The encrypted message, and the mixed up alphabet. The function should return a string that is the same as the original unencrypted message.
'''


def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

def decrypt(encrypted, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ''
    for char in encrypted:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted


cipher = "badcfehgjilknmporqtsvuxwzy"

encrypted = encrypt('hello world', cipher)
print (encrypted)

decrypted = decrypt(encrypted, cipher)
print(decrypted)
