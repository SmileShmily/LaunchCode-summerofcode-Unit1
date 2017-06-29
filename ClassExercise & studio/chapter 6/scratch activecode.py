lst=[False,False,True,True]
def any(lst):
    '''returns true if any item in list is true ,else return false'''
    for x in lst:
        if x==True:
            return True
        #else :
    return False
print(any(lst))