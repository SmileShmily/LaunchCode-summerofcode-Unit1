def caesarCipher(t, s):
    """
        caesarCipher(t, s)

        Returns the cipher text in a given plain text or vice versa.

        Variables:
            t - text (input), nt - new text (output)
            lc - lowercase, uc - uppercase
            pt[c] - nth character of the plain text (also used to get the
            plaintext in a given cipher text.
        Description:
            In Cryptography, caesar cipher is the most simplest and most widely
            known encryption/decryption techniques. It substitutes your input
            with a given shift (s). e.g, if s is 1, A will be B
            or a will be b.
        Examples:
            #>>> #caesarCipher("Be sure to drink your ovaltine", 13)
            'Or fher gb qevax lbhe binygvar'
            #>>> caesarCipher("Or fher gb qevax lbhe binygvar", -13)
            'Be sure to drink your ovaltine'
    """
    nt = ""
    t = t.replace("\n", "")

    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lc = "abcdefghijklmnopqrstuvwxyz"

    for c in range(len(t)):
        if (t[c].isalpha()):
            if (t[c].isupper()):
                nt += uc[(uc.index(t[c]) + s) % 26]
            else:
                nt += lc[(lc.index(t[c]) + s) % 26]
        else:
            nt += t[c]


    return nt