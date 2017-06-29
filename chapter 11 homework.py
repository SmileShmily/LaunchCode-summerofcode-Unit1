'''
Chapter 11 Assignment
Write a function that will sum up all the elements in a list up to but not including the first even number.
'''

def sum_of_initial_odds(nums):
    # your code here
    "Sum all the elements in a list up to but not including the first even number."
    count = 0
    for i in nums:
        if i % 2 == 0:
            break
        count += i
    return count
#print ("even sum in 8 1 7 5 8:", sum_of_initial_odds([8,1,7,5,8]))

   # [Executed at: Thu Jul 14 9:15:35 PDT 2016]
  # 1 Your code passed all the tests!