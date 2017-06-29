letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
'''
def alphabet_position(letter):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    ## Whether the text is for the letter, if it is, then determine the size of the write, respectively, to encrypt
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in letter )
    '''
def alphabet_position(letter):
    if len(letter) == 1:
        return ord(letter.upper()) - 65
    rot = []
    for ch in letter:
        rot.append(ord(ch.upper()) - 65)
    return rot
def rotate_character(char, rot):
    ciphertext = ""
    ## Whether the text is for the letter, if it is, then determine the size of the write, respectively, to encrypt
    for ch in char:
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + rot) % 26]
            else:
                ciphertext += letter_list[(ord(ch) - 97 + rot) % 26].lower()
    # If the cipher text is not a letter, it is added directly to the cipher text string.
        else:
            ciphertext += ch
    return ciphertext
def encrypt(text, rot):
    #letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ""
    i = 0
    for ch in text:
        if 0 == i % len(rot):
            i = 0
        if ch.isalpha():
            if ch.isupper():
                ciphertext += letter_list[(ord(ch) - 65 + rot[i]) % 26]
                i += 1
            else:
                ciphertext += letter_list[(ord(ch) - 97 + rot[i]) % 26].lower()
                i += 1
        else:
            ciphertext += ch
    return ciphertext
