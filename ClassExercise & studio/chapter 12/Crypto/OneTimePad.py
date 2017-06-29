# output is binary ( 0bXXXXXXXX ), if you need a string
# look at hexlify and unhexlify in the binascii module
def otp(message, key):
	if len(key) < len(message):
		print("Key is too small")
		return None
	else:
		crypt_msg = ''.join([bin(ord(a) ^ ord(b)) for a, b in zip(key, message)])
		print(crypt_msg)
		return crypt_msg

# Using otp key more than once is not a good idea and this is why:
# (m1 Xor key) Xor (m2 Xor key) = m1 Xor m2
# Note: anything outside [a-z][A-Z][0-9] isn't taken into account for this.

# For the knowledge:
# binary letter: a = 01100001; z = 01111010; A = 01000001; Z = 01011010.
# binary number: 0 = 00110000; 9 = 00111001.
# binary space = 00100000

# Fun part:
# a Xor space = A and A Xor space = a
# if m1 Xor m2 = 01XXXXXX <=> letter Xor (number or space)
# if m1 Xor m2 = 00XXXXXX <=> letter Xor letter OR number Xor (number or space)
# Note: a something Xored with itself will give 00000000

def Xor(m1, m2):
	Xored = ""
	size = max(len(m1), len(m2))
	for x in range (0, size):
		if m1[x] == m2[x]:
			Xored += "0"
		else:
			Xored += "1"
	return Xored

# This is assuming you only have 2 messages.
# If you have more you can cross match the "spaces" to get known letters.

def mtpcrack(message1, message2):
	if len(message1) % 8 != 0 or len(message2) % 8 != 0:
		print("Problem with messages")
		return None
	else:
		Xored    = Xor(message1, message2)
		cutXor   = [Xored[i:i+8] for i in range(0, len(Xored), 8)]
		cutwords = []
		tmpwords = ""
		# Cut into words
		for letter in cutXor:
			tmpletter = int(letter,2)
			if tmpletter > 63:
				#This can be considered as "letter Xor space" most of the time
				print("This letter should be: " + chr(int(letter,2) ^ ord(" ")))
				print("(If this looks weird, then it's a number!)")
			else:
				print("Possible letters:")
				# if A- or Z-a or z+ the letter is not correct
				# <=> 90 < val < 97 or val < 65 or val > 122
				possletters = ""
				for val in range(97, 123):
					tmp = val ^ tmpletter
					if (tmp > 64 and tmp < 91) or (tmp > 96 and tmp < 123):
						possletters += chr(tmp) + " "
				print(possletters)
				# No need to do 65-90 because it'll just give uppercase.
			dump = input("Press enter for the next letter")

		# Right here you could add a "check in a dictionary before printing"
		# to know if the word exists or not.
# BUT complexity would explode -> O(26^l), l being the length of the word...