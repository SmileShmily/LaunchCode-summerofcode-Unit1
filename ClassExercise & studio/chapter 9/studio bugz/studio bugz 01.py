'''Today’s studio, rather than explicitly pertaining to Strings, is more of an overall review.
You will get some practice debugging a variety of common mistakes that new coders make.

Below are a handful of code snippets that are broken. See if you can fix them!

    The function below, print_every(i, nums) receives a list of numbers nums, along with an integer i.
    The function is supposed to print every ith element from the list. But it’s not working!

'''

# in a list of numbers, print every ith number
def print_every(i, nums):
    counter = 0
    for a in nums:
        if counter % i == 0:
            print(a)
        counter+=1

print_every(3, [4, 7, 2, 8, 1, 0, 9, 6])
# should print 4, then print 8, then print 9