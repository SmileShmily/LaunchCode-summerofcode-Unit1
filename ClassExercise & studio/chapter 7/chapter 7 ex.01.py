'''Add a print statement to Newton’s sqrt function that prints out better each time it is calculated.
 Call your modified function with 25 as an argument and record the results.
'''
def newtonSqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        print("Approx:", better)
    return approx


print("Final approx:", newtonSqrt(25))
