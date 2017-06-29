'''
def is_sorted(lst, key=lambda x, y: x < y):
    for i, el in enumerate(lst[1:]):
        if key(el, lst[i-1]):
            return False
    return True
'''
def is_sorted(lst):
    it = iter(lst)
    try:
        prev = it.next()
    except StopIteration:
        return True
    for x in it:
        if prev > x:
            return False
        prev = x
    return True
