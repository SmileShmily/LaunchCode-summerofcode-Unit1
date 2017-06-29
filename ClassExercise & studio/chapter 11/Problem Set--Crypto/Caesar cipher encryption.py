'''
alpha = ['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x',
         'y', 'z']

shift = range(26)


def user_info():
    info = input("\nPress 'e' to encrypt or 'd' to decrypt: ").lower()
    if info == 'e' or 'd':
        return info


def user_message():
    code = input("What is your message?: ")
    return code


def user_shift():
    shift = int(input("What is your shift number?: "))
    while True:
        if shift == int(shift):
            return shift


def True_Message(info, code, shift):
    if info[0] == 'd':  # This encrypts the code
        shift = -shift

    for letter in code:
        if letter in alpha:
            alpha_2 = ord(letter) + shift
        secret_message = ""
    if alpha_2 in range(0, len(alpha)):
        final_mix = chr(alpha)
        secret_message += final_mix


    return secret_message

info = user_info()
code = user_message()
shift = user_shift()
print(True_Message(info, code, shift))
'''
alpha = ['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x',
         'y', 'z']

shift = range(26)


def user_info():
    info = input("\nPress 'e' to encrypt or 'd' to decrypt: ").lower()
    if info in ('e', 'd'):  # 'or' does not work how you think it does
        return info


def user_message():
    code = input("What is your message?: ")
    return code


def user_shift():
    while True:
        shift = int(input("What is your shift number?: "))
        if shift == int(shift):
            return shift


def True_Message(info, code, shift):
    if info[0] == 'd':  # This encrypts the code
        shift = -shift

    for letter in code:
        if letter in alpha:
            alpha_2 = ord(letter) + shift
            secret_message = ""
    if alpha_2 in range(0, len(alpha)):
        final_mix = chr(alpha)
        secret_message += final_mix

    return secret_message
info = user_info()
code = user_message()
shift = user_shift()
print(True_Message(info, code, shift))
