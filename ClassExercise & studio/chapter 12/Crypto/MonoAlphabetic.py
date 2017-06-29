# Definition
# This is a substitution algorithm
# It basically pairs every letter in the alphabet with one another
# and substitutes these letters in the message
# This is a version where you just give it a dictionary with the letters

# Encrypt
# key is letter -> substitution
# Decrypt
# key is substitution -> letter

# Warning spaces uppercase and lowercase are not modified: 'A' != 'a'
def monoalphabetic(message, key):
	crypt_msg = ''.join(key[letter] for letter in message)
	print(crypt_msg)
	return crypt_msg

# The smart way of cracking it would be through a statistical attack since
# this is a substitution algorithm, but I'd rather do it the hard way, so
# lets bruteforce it!
# We could use a dictionary to know if words exist and make it an automated
# task, or you could go through 52! combinations (a -> z + A -> Z)