def vigenereCipher(t, s, m=0):
    """
        vigenereCipher(t, s, m=0)

        Returns the cipher text in a given plain text or vice versa.

        Variables:
            t - text (input), nt - new text (output)
            lc - lowercase, uc - uppercase
            t[c] - nth character of the plaintext (also used to get the
            plaintext in a given cipher text.
            nt[c] - the nth character of the cyphertext in the formula.

        Description:
            In Cryptography, vigenere cipher is a secured cipher which allows
            you to encrypt your plaintext with letters and numbers.
        Modes:
            If m is 0, it encrypts, if it is set to 1, it decrypts.

        Formula:
            Encryption Formula -> nt[c] = (t[c] + s[c]) % 26
            Decryption Formula -> nt[c] = (t[c] - s[c]) % 26

        Examples:
           # >>> vigenereCipher("ATTACKATDAWN", "LEMONLEMONLE")
            'LXFOPVEFRNHR'

            #>>> vigenereCipher('LXFOPVEFRNHR', "LEMONLEMONLE", 1)
            'ATTACKATDAWN'
    """

    nt = ""
    t = t.replace("\n", "")

    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lc = "abcdefghijklmnopqrstuvwxyz"
    n = "0123456789"
    for c in range(len(t)):
        if (m == 0):
            if (t[c].isalpha()):
                if (t[c].isupper()):
                    if (s[c] in n):
                        nt += uc[(uc.index(t[c]) + n.index(s[c])) % 26]
                    else:
                        nt += uc[(uc.index(t[c]) + uc.index(s[c])) % 26]
                else:
                    if (s[c] in n):
                        nt += uc[(uc.index(t[c]) + n.index(s[c])) % 26]
                    else:
                        nt += lc[(lc.index(t[c]) + lc.index(s[c])) % 26]
            else:
                nt += t[c]
        elif (m == 1):
            if (t[c].isalpha()):
                if (t[c].isupper()):
                    if (s[c] in n):
                        nt += uc[(uc.index(t[c]) - n.index(s[c])) % 26]
                    else:
                        nt += uc[(uc.index(t[c]) - uc.index(s[c])) % 26]
                else:
                    if (s[c] in n):
                        nt += uc[(uc.index(t[c]) - n.index(s[c])) % 26]
                    else:
                        nt += lc[(lc.index(t[c]) - lc.index(s[c])) % 26]
            else:
                nt += t[c]
        else:
            return "Mode doesn't exist!"
    return nt
