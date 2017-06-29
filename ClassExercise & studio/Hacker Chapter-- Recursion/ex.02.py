'''Write a recursive function to reverse a list.
'''
mylist = [1, 2, 3, 4, 5]
backwards = lambda l: (backwards (l[1:]) + l[:1] if l else [])
print (backwards (mylist))


#fangfa 2
def reverse(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return reverse(alist[1:]) + alist[0]
print(reverse('1,2,3,4,5'))
print(reverse('a,b,c,d,e,f,g'))