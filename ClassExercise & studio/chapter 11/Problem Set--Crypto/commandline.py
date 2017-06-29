'''
    commandline.py

    Jeff Ondich, 21 April 2009

    This program gives a brief illustration of the use of
    command-line arguments in Python.  The program accepts
    a file name from the command line, opens the file, and
    counts the lines in the file.
'''

import sys

# If the user types too few or too many command-line arguments,
# this code prints a usage statement and exits the program.
# Note that sys.argv[0] is the name of the program, so if
# I type "python commandline.py something", then sys.argv[0]
# is "commandline.py" and sys.argv[1] is "something".
if len(sys.argv) != 2:
    print ('Usage:', sys.argv[0], 'filename')
    exit()

# You don't normally need to tell the users what they just
# typed, but the print statement here just verifies that
# we have grabbed the right string for the file name.
fileName = sys.argv[1]
print ('The requested file is', fileName)
theFile = open(fileName)

# Count the lines in the file.
lineCounter = 0
for line in theFile:
    lineCounter = lineCounter + 1

# Report the results.
print ('The file', fileName, 'contains', lineCounter, 'lines.')

# Clean up after yourself.
theFile.close()
