'''

    Write a function that sums the positive even numbers in a list of integer values.
    The function should be called sum_positive_even and should accept a single list as a parameter.
    Your function should return an integer value. If there are no positive even integer values in the list, then your function should return 0.
     For example:

    test_list = [1, 2, 3, 4]
    print(sum_positive_even(test_list)) 6
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