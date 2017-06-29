''')

(GRADED) Write a function that will sum up all the elements in a list up to but not including the first even number.

'''

def sumexclude(data):
    "Sum all the elements in a list up to but not including the first even number."
    count = 0
    for i in data:
        if i % 2 == 0:
            break
        count += i
    return count
print ("even sum in 8 1 7 5 8:", sumexclude([8,1,7,5,8]))