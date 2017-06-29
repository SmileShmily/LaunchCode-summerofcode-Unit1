'''
def removeVowels(s):
    vowels = "aeiouAEIOU"
    sWithoutVowels = ""
    for eachChar in s:
        if eachChar not in vowels:
            sWithoutVowels = sWithoutVowels + eachChar
    return sWithoutVowels

print(removeVowels("compsci"))
print(removeVowels("aAbEefIijOopUus"))
'''

myname=input("what's your name:")
#myname = "Edgar Allan Poe"
namelist = myname.split()
init = ""
for aname in namelist:
    init = init + aname[0].upper()
print("The initials of '",myname, "'are", "'",init,"'")

'''answer = get_initials("Ozzie Smith")
print("The initials of 'Ozzie Smith' are", answer)
'''