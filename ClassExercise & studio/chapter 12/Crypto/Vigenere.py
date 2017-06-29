def vigenere_encode(message, key):
	# I'm lazy that's why
	message = message.lower()
	key = key.lower()
	# Spaces aren't letters
	message = message.replace(' ','')
	key = key.replace(' ','')
	# Make the key at least the same size as the message
	key = key * int(len(message) / len(key) + 1)
	# The math: (letter_from_message + letter_from_key) mod 26 = crypted_letter
	# 97 is the ascii code for 'a'
	crypt_msg = ''.join([chr((((ord(a) - 97) + (ord(b) - 97)) % 26) + 97) for a, b in zip(message, key)])
	print(crypt_msg)
	return crypt_msg

def vigenere_decode(message, key):
	message = message.lower()
	key = key.lower()
	message = message.replace(' ','')
	key = key.replace(' ','')
	key = key * int(len(message) / len(key) + 1)
	crypt_msg = ''.join([chr((((ord(a) - 97) - (ord(b) - 97)) % 26) + 97) for a, b in zip(message, key)])
	print(crypt_msg)
	return crypt_msg

# The method would be to:
# First you need to "guess" the key length with math
# Then, since you know the size of the key, you can "encode" parts of the text with itself
# which drops the key. Why? Because of modulo magic of course!
# Finally a frequency analysis should do the trick

# What happens if the key is the size of the message you say?
# Well in that particular case, it's not called a Vigenere cipher. Problem solved.
# (See running key cipher)

#def vigenere_crack(message):