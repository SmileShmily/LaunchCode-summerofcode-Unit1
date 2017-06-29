'''Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the minimum and maximum score for each student.
Print out their name as well.
'''
f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))

f.close()
