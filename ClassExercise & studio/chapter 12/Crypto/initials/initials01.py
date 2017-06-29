'''
def main():
    full_name = raw_input('Type your name and press ENTER. ')
    initials = '.'.join(name[0].upper() for name in full_name.split())
    print(initials)
    '''

'''
#def main():


    name = input('Type your name and press ENTER. ')
    name_list = name.split()

    print(name_list)

    first = name_list[0][0]
    second = name_list[1][0]
    last = name_list[2][0]

    print(first.upper(),'.', second.upper(),'.', last.upper())


#main()
'''


def whatDoIdo(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    tmp = ""  # tmp is initialized to the empty string
    for ch in str:
        x = alphabet.find(ch)
        y = (x + 13) % 26
        tmp = tmp + alphabet[y]

    return tmp


print(whatDoIdo("clguba") )
print(whatDoIdo(whatDoIdo("hello")))
