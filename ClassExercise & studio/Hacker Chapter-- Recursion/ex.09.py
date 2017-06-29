'''Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug.
Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water.
 How can you get exactly two gallons of water in the 4-gallon jug?
'''
import os
import os.path
def listDirectory(dir, indent):
    lists = os.listdir(dir)
    for i in lists:
        filename = dir + '/' + i
        if os.path.isfile(filename):
            print('%s%s' % (' '*indent, i))
        elif os.path.isdir(filename):
            print('%s%s/' % (' '*indent, i))
            listDirectory(filename, indent + 4)


if __name__ == '__main__':
    listDirectory('/Users/shenshen/Pictures', 0)