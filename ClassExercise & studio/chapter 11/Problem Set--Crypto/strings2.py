'''strings2.py

   Jeff Ondich, 2 April 2009

   This sample program will introduce you to "iteration" or
   "looping" over the characters in a string.
'''

s = 'two kudus and a newt'

# What happens here?
print('The first loop')
for ch in s:
    print (ch)
print()


# And here?
print( 'The second loop')
k = 0
while k < len(s):
    print (s[k])
    k = k + 1
print()

# Can you make sense of these structures?  Let's talk about
# them on Monday.