'''Write a function called removeDups that takes a string and creates a new string by only adding those characters
that are not already present. In other words, there will never be a duplicate letter added to the new string.
'''

def removeDups(astring):
    # your code here
    return ''.join(set(astring))

print(removeDups("mississippi"))   #should print misp
