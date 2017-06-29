"""Write a function is_rightangled which, given the length of three sides of
    a triangle, will determine whether the triangle is right-angled. Assume that
    the third argument to the function is always the longest side. It will return
    True if the triangle is right-angled, or False otherwise.
    Extend the (above) program so that the sides can be given to the function in
    any order."""
from test import testEqual


def is_rightangled(a, b, c):
    # your code here
    # Sorting the list to pin down the biggest number.
    L = sorted([a, b, c])
    # Another way would be to rest = L.remove(max(L))
    # Plus big = set(L) & set(rest) (or {L} & {rest} if using tuples and nex
    # set literal syntax in py2.7 or py3.
    # Keeping the order: [i for i, j in zip(L, rest) if i == j]
    # Or inverted: big = max([a,b,c]) and rest = L.remove(big)
    epsilon = 0.001
    result = L[0] ** 2 + L[1] ** 2
    if abs(L[2] ** 2 - result) < epsilon:
        return True
    else:
        return False


testEqual(is_rightangled(1.5, 2.0, 2.5), True)
testEqual(is_rightangled(4.0, 8.0, 16.0), False)
testEqual(is_rightangled(4.1, 8.2, 9.1678787077), True)
testEqual(is_rightangled(4.1, 8.2, 9.16787), True)
testEqual(is_rightangled(4.1, 8.2, 9.168), False)
testEqual(is_rightangled(0.5, 0.4, 0.64031), True)
