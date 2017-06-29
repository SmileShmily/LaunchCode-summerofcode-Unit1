def is_palindrome(string):
    '''is the string to palindrome'''
    string=string.lower()
    length=len(string)
    for pos in range(0,length):
        if string[-(pos+1)]!=string[pos]:
            return False
        return True
print(is_palindrome("hannch"))
print (is_palindrome("racecar"))
print (is_palindrome("palindrome"))