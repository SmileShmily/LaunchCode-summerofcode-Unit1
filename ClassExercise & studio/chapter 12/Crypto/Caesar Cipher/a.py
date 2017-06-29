import codecs
s  = "hello,world"
os = codecs.encode( s, "rot13" )
print(os)


import codecs

print(codecs.encode("hello", "rot-13"))


import codecs

s   = "Hello"
enc = codecs.getencoder( "rot-13" )
os  = enc( s )[0]

print( os ) # "Uryyb"