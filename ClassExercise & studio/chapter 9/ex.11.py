'''Write a function called rot13 that uses the Caesar cipher to encrypt a message.
The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to ‘its right’
 in the alphabet. So for example the letter a becomes the letter n. If a letter is past the middle of the alphabet
  then the counting wraps around to the letter a again, so n becomes a, o becomes b and so on.
  Hint: Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic.'''

def rot13(mess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + 13
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted

print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
