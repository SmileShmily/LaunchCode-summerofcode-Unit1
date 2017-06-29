'''Since a string is just a sequence of characters, they can be sorted from least to greatest.
Sorting can be hard so we’re just going to check if a string is sorted.
Write a function which returns a boolean indicating if the string is sorted or not.

Here’s an example of how your function should behave.

is_sorted("ABC") == True
is_sorted("aBc") == False
is_sorted("dog") == False

'''

'''def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    # TODO: Fill in details
    s="string"
    s="".join((lambda x:(x.sort(),x)[1])(list(s)))
#string=string.upper()
#length=len(string)
    for x in range s:
        if s==(s[x] >= 'A' and s[x] <= 'Z'):
            return True
        return False
print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))'''


def is_sorted(t):
    for i in range(len(t) - 1):
        if t[i + 1] < t[i]:
            return False
    return True
print(is_sorted("ABC"))
print(is_sorted("aBc"))
print(is_sorted("dog"))