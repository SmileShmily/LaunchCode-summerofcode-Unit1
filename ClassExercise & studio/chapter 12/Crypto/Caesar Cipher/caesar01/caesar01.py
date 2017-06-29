def caesarCipher(pt, s, m=0):
    """
        caesarCipher(pt, s, m=0)

        Returns the cipher text in a given plain text or vice versa.

        Variables:
            ct - ciphertext, pt - plaintext
            lc - lowercase, uc - uppercase
            m - mode, s - shift
            pt[c] - nth character of the plain text (also used to get the
            plaintext in a given cipher text.
        Description:
            In Cryptography, caesar cipher is the most simplest and most widely
            known encryption/decryption techniques. It substitutes your input
            with a given shift (s). e.g, if s is 1, A will be B
            or a will be b.

        Modes:
            m is set to 0 by default which encrypts. it will decrypt the cypher
            if m is set to 1 by adding it as a parameter.
        Examples:
            >>> #caesarCipher("Be sure to drink your ovaltine", 13)
            Ciphertext:
              Or fher gb qevax lbhe binygvar
            'Program finished without any errors.'
            >>> #caesarCipher("Or fher gb qevax lbhe binygvar", 13, 1)
            Plaintext:
              Be sure to drink your ovaltine
            'Program finished without any errors.'
    """

    uc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"
        , "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
        , "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ct = ""

    if (m == 0):
        for c in range(len(pt)):
            if (pt[c].isalpha()):
                if (pt[c].isupper()):
                    ct += uc[(uc.index(pt[c]) + s) % 26]
                else:
                    ct += lc[(lc.index(pt[c]) + s) % 26]
            else:
                ct += pt[c]

        print("Ciphertext:\n  " + ct)

    elif (m == 1):
        for c in range(len(pt)):
            if (pt[c].isalpha()):
                if (pt[c].isupper()):
                    ct += uc[(uc.index(pt[c]) - s) % 26]
                else:
                    ct += lc[(lc.index(pt[c]) - s) % 26]
            else:
                ct += pt[c]

        print("Plaintext:\n  " + ct)

    else:
        return "That mode doesn't exist."

    return "Program finished without any errors."

