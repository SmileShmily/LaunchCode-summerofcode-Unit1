# This is a substitution algorithm
# But we replace letters with symbols.
# They look horrible in ascii but you'll get the point.
# Note:
# To make it harder, a symbol could be a word! (see Babington Plot)

def pigpen(message):
	key = {
	'a' : "_|",
	'b' : "|_|",
	'c' : "|_",
	'd' : "=|",
	'e' : "|=|",
	'f' : "|=",
	'g' : "-|",
	'h' : "|-|",
	'i' : "|-",
	'j' : "_.|",
	'k' : "|._|",
	'l' : "|._",
	'm' : "=.|",
	'n' : "|.=|",
	'o' : "|.=",
	'p' : "-.|",
	'q' : "|.-|",
	'r' : "|.-",
	's' : "\\/",
	't' : ">",
	'u' : "<",
	'v' : "/\\",
	'w' : "\\./",
	'x' : ".>",
	'y' : "<.",
	'z' : "/.\\",
	' ' : "   "}
	crypt_msg = ''.join(key[letter.lower()]+' ' for letter in message)
	print(crypt_msg)
	return crypt_msg

# To crack this we would need to know the relationship symbol -> letter is.
# Here we know "_|" is 'a' so it's easy to do, but we could turn "_|" into
# "<(^_^<)<(^_^)>(>^_^)>" and as long as you can't reproduce that specific
# symbol chain with another letter it would work.
# Guessing them wouldn't be that hard though.