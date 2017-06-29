def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False

	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1

	    return found
alist=[5,6,8,9,45,85]
item=85
print(binarySearch(alist, item))