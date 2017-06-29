# a = 97; z = 122; A = 65; Z = 90.

# Shift right by 3
def caesar_encode(message):
	crypt_msg = ""
	for letter in message:
		if letter.isalpha():
			tmp = ord(letter) + 3
			if (tmp > 122) or (tmp > 90 and tmp < 97):
				crypt_msg += chr(tmp - 26)
			else:
				crypt_msg += chr(tmp)
		else:
			crypt_msg += letter
	print(crypt_msg)
	return crypt_msg

# Shift left by 3
def caesar_decode(crypt_msg):
	message = ""
	for letter in crypt_msg:
		if letter.isalpha():
			tmp = ord(letter) - 3
			if (tmp < 65) or (tmp < 97 and tmp > 65):
				message += chr(tmp + 26)
			else:
				message += chr(tmp)
		else:
			message += letter
	print(message)
	return message

# 26 possibilities to check, faster than frequency attack
def caesar_bruteforce(crypt_msg):
	for shift in range(0,25):
		message = ""
		for letter in crypt_msg:
			if letter.isalpha():
				tmp = ord(letter) - shift
				if (tmp < 65) or (tmp < 97 and tmp > 65):
					message += chr(tmp + 26)
				else:
					message += chr(tmp)
			else:
				message += letter
		print(message)
		entry = input("Can you read the message? (y-n)\n")
		if entry == "y":
			return message
	print("This is not a caesar encryption")
