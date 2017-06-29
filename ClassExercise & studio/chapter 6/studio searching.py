'''Write a function that takes two arguments: a list of numbers (either floats or integers, or mixed), along with a single number.
 The function should return True if the number is in the list, and False otherwise.

If you solve that problem with time to spare, modify your function so that it takes the same arguments,
but returns the number of times that the number appears in the list.
'''
#class studio

def contains_n(numbers, n):
    # Your code here, to replace this non-working version
     for x in numbers:
        if x==n:
            return True
     return False

# Be sure to test your function with various inputs
numbers=[0.25,23,4,82,1.23]
n=1.23
print(contains_n(numbers, n))

'''def contains_n(numbers, n):
    # Your code here, to replace this non-working version
     for x in numbers:
        if x==n:
            return True
     return False

# Be sure to test your function with various inputs
nums1=[0.25,23,4,82,1.23]
nums2=[5,6.5,0.23]
n=0.25
print(contains_n(nums1, n))
print(contains_n(nums2, n))
'''

