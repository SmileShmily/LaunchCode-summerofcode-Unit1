'''def countVowels(s):
    s = s.lower() #so you don't have to worry about upper and lower cases
    vowels = 'aeiou'
    return {vowel:s.count(vowel) for vowel in vowels} #a bit inefficient, but easy to understand'''
'''
n = "Hello"
# Your function here!
def string_function(s):
    return s + 'world'
print (string_function(n))'''
'''
if __name__ == '__main__':
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if (letter in 'O') or (letter in 'Q'):
            letter = letter + 'u'
print (letter + suffix)'''


def rotate_word(word, rotate_num):
    # a = 97, z = 122, A = 65, Z = 90
    new_word = ''
    base_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"
    lookup_table = ''

    # Cut off the rotation number
    # assume this is a positive number for now
    rotate_portion = base_table[:rotate_num]

    # Run through the chars in base_table
    # Append to the end of lookup_table
    for char in base_table[rotate_num:]:
        # populate the lookup_table, starting at the rotated number
        lookup_table = lookup_table + char
    # ...then append rotated portion to the tail end
    lookup_table = lookup_table + rotate_portion

    for char in word:
        # if it is alphanumeric
        if char.isalnum():
            # Find the first instance of the char in the base_table
            index = base_table.find(char, 1)
            # then lookup up this index in the lookup_table
            new_word = new_word + lookup_table[index]
        # else, keep the character as it is.
        else:
            new_word = new_word + char
    return new_word


if __name__ == '__main__':
    # print rotate_word('banana', 13)
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    print(rotate_word("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 13))
    print("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")
    print(rotate_word("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.", 13))