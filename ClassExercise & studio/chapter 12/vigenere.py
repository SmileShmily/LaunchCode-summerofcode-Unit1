# MA2317 introduction to number theory
# Vigenere cipher
import string

def encipher(plaintext_file_name,ciphertext_file_name,key):
	N=len(key)
	n=0
	src=open(plaintext_file_name)
	dest=open(ciphertext_file_name,"w")
	for line in src.readlines():	
		line1=""	
		for c in line.lower():
        		if 'a'<=c<='z':
		   		line1 += chr(ord('a')+(ord(c)-2*ord('a')+ord(key[n % N]))%26)
				n+=1;
			else: line1+=c
		dest.write(line1)
    	return n

def decipher(ciphertext_file_name,decipheredtext_file_name,key):
	key1="";
	for i in range(len(key)): key1+=chr(ord('a')+(26-ord(key[i])+ord('a'))%26)
	return encipher(ciphertext_file_name,decipheredtext_file_name,key1);


# letter frequencies from all chracters on the positions = a mod n in file_name
def get_frequencies(file_name,a=0,n=1):
	F = dict([(c,0.0) for c in string.lowercase])	
	N=0
	Na=0
	f = open(file_name)
	for line in f.readlines():
		for c in line.lower():
        		if 'a'<=c<='z':
            			if N % n == a:
					Na += 1
					F[c] += 1
				N += 1
	for c in string.lowercase:
		F[c]=F[c]/Na
	if n==1: 
		print("number of processed characters: ")
		print Na
	return F

# distance between two sets of letter frequencies
def distance(F1,F2):
	dm=0.0
	for c in string.lowercase:
		d=abs(F1[c]-F2[c])
		if d>dm: dm=d
	return dm

# shift of the set of frequensies by letter a: c -> F[c+a]
def shift(F,a):
	F1 = dict([(c,0) for c in string.lowercase])
	for c in string.lowercase:
		F1[c]=F[chr(ord('a')+(ord(c)-2*ord('a')+ord(a))%26)]
	return F1

# find letter a such that the distance between F2 and F1 shifted by a is minimal; returns a and this minimal distance 
def best_shift(F1,F2):
	dm=1.0
	a='a'
	for c in string.lowercase:
		ds = distance(shift(F1,c),F2) 
		if ds<dm:
			dm=ds
			a=c
	return [a,dm]	

# find the best key of length n using F as a template set of frequncies
def get_key(ciphertext_file_name,F,n):
	d=0.0
	key=""
	K = dict([(a,best_shift(get_frequencies(ciphertext_file_name,a,n),F)) for a in range(n) ])	
	for a in range(n):
		if K[a][1]>d: d=K[a][1]
		key+=K[a][0]
	return [key,d]
