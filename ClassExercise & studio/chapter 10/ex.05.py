''')

(GRADED) Write a function to find the sum of all the even numbers in a list.
'''
'''
#1
for i in range(0, 11, 2):
    print(i)
sum(range(0, 11, 2))
#2
sum = 0
for i in range(0, 11, 2):
    print(i)
    sum += i
'''

'''
#import math
def addEvenNumbers(start,end):
  total = 0
  if end%2==0:
    for x in range(start,end):
      if x%2==0:
        total+=x
    return total+end
  else:
    for x in range(start,end):
      if x%2==0:
        total+=x
    return total
print (addEvenNumbers(4,12))
'''
'''
def sum_positive_even(lst):
    return sum(filter(lambda x: x > 0 and x%2 == 0, lst))

def sum_positive_even_v2(lst):
    sum = 0
    for i in lst:
        if i%2==0 and i>0:
            # remember that item by summing it up (don't return it yet)
            sum+=i
        # else: do nothing and check the next item
    # all the list has been checked
    return sum

test_list = [-2, -1, 0, 1, 2, 3, 4]

print(sum_positive_even(test_list))
print(sum_positive_even_v2(test_list))
'''
#solve 1
my_list = [1, 3, 5, 6, 8, 10, 34, 2, 0, 3]
even_list = filter(lambda x: x%2 == 0, my_list)
print(sum(even_list))



#solve 2
myList = [1, 3, 5, 6, 8, 10, 34, 2, 0, 3]
result = 0  # Initialize your results variable.
for i in myList:  # Loop through each element of the list.
   if not i % 2:  # Test for even numbers.
     result += i
print(result)


#myself did
data= [1, 3, 5, 6, 8, 10, 34, 2, 0, 3]
def sumeven(data):
    "Sum up all the even numbers in a list."
    return sum(i for i in data if i % 2 == 0)
print(sumeven(data))