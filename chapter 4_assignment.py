import math
#Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
#Write a loop that prints each of the numbers on a new line, like this:
#12
#10
#...etc
#Then, write a loop that prints each number and its square on a new line, like this:
#The square of 12 is 144
#The square of 10 is 100
#...etc

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# TODO 1 
# print each number on a new line
# your code here:
for elem in nums:
    print(elem)

# TODO 2 
# print the square root of each number on a new line
# your code here:
# print(elem**2,sep='\n')
a=[b**2 for b in nums]
# c=a+nums
# c.sort()
print("The square of",nums[0],"is",a[0])
print("The square of",nums[1],"is",a[1])
print("The square of",nums[2],"is",a[2])
print("The square of",nums[3],"is",a[3])
print("The square of",nums[4],"is",a[4])
print("The square of",nums[5],"is",a[5])
print("The square of",nums[6],"is",a[6])
print("The square of",nums[7],"is",a[7])
print("The square of",nums[8],"is",a[8])
