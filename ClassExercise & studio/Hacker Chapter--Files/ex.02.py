'''Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each student,
and print out the student’s name along with their average grade.
'''

'''
def students_avg():
    """Using the text file studentdata.txt (shown in exercise 1) write a program
    that calculates the average grade for each student, and print out the student’s
    name along with their average grade."""

    with open("lib/students.txt", "r") as f:
        for i in f:
            line = i.split()
            avg = sum(float(i) for i in line[1:]) / len(line)


print("Name: %s, Avg: %.2f" % (line[0], avg))
'''
f = open("studentdata.txt", "r")
for i in f:
    line = i.split()
    avg = sum(float(i) for i in line[1:])/len(line)
print ("Name: %s, Avg: %.2f" % (line[0], avg))
