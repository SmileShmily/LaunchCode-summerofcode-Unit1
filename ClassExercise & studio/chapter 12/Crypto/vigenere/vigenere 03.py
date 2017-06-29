def cesar(message, cle):
    """
    Décale tous les (codes de) caractères de message de la valeur cle ;
    message est supposé ne contenir que des lettres (non accentuées) minuscules
    """

    code = ''        # le message codé
    ord_a = ord('a') # valeur utilisée plusieurs fois

    for c in message:
        offset_c = ord(c) - ord_a      # rang du caractère c dans l'alphabet
        offset_d = (offset_c + cle)%26 # d est le codage de c
        d = chr(offset_d + ord_a)
        code = code + d

    return code

def vigenere(message, cle):
    """
    Les paramètres message et cle sont des chaînes de caractères ne comportant
    que des lettres non accentuées (ascii) minuscules. Décale chaque (code de)
    caractère de message du rang du caractère correspondant dans cle
    """
    code = ''

    len_cle = len(cle)
    for i in range(len(message)):
        m = message[i]                # caractère à coder
        c = cle[i%len_cle]            # caractère correspondant dans cle
        offset_c = ord(c) - ord('a')  # rang de c
        d = cesar(m, offset_c)
        code += d
    return code