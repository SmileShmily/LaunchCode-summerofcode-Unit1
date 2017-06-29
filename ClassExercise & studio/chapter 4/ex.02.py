'''Turtle objects have methods and attributes. For example, a turtle has a position and when you move the turtle forward, the position changes.
Think about the other methods shown in the summary above. Which attibutes, if any, does each method relate to? Does the method change the attribute?
'''

'''Write a program that prints out the lyrics to the song “99 Bottles of Beer on the Wall”

'''
for i in range(99, -1, -1):
    if i==1:
        print (i,"bottle of beer on the wall,",i,"bottle of beer.")
        print ("Take one down and pass it around,")
        print (i-1,"bottles of beer on the wall.")
    elif i==0:
        print( "No more bottles of beer on the wall.  How about some soju?")
    else:
        print (i,"bottles of beer on the wall,",i,"bottles of beer.")
        print ("Take one down and pass it around,")
        print (i-1,"bottles of beer on the wall.")