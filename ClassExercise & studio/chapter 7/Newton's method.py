def sqrt(x):
    a=0.5*x
    b=x
    while abs(a-b)>0.001:
        b=a
        a=0.5*(a+x/a)
    return a