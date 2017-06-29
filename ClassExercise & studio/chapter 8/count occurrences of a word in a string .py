def count(sequence,item):
    total=0 #counter

    if type(sequence)==list: #the if works for a list or list of lists
        for element in sequence:
            if element ==item:
                total+=1
    else: #the else works for strings, where item is a word
        sequence=sequence.replace(',','') #remove commas
        sequence=sequence.replace('.','') #remove periods
        sequence=sequence.lower() #make lowercase
        for word in sequence.split():  #will iterate through words instead of characters
            if word==item:
                total+=1
    return total

print (count("Help me rhonda, help me Rhonda.", "rhonda"))
print (count([1,1,1,2],1))
print (count([[1,1], [1,2], [1,1]], [1,1]))