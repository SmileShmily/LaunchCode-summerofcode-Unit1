'''
    You are the bouncer outside the door of a seniors only bar.
     People must be 70 or older, otherwise they are not allowed in.
     When a group of friends arrives, your job is to determine whether to accept or reject the group.
     The function below, check_group, is supposed to return a boolean indicating whether or not the group is allowed inside.
     But it’s not working!

'''


# return True if every member of the group is at least 70, otherwise return False
def check_group(ages):
    for age in ages:
        if age < 70:
            return False
    return True


from test import testEqual

# this group should not be allowed inside the bar
group = [78, 71, 25, 84]
testEqual(check_group(group), False)

# this group should also not be allowed inside the bar
group2 = [ 2, 99 ]
testEqual(check_group(group2), False)

# this loner is allowed
group3 = [ 99 ]
testEqual(check_group(group3), True)
