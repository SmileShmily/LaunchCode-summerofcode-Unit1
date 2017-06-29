'''Write a recursive function to compute the Fibonacci sequence.
How does the performance of the recursive function compare to that of an iterative version?
'''

def fibonacci_ite(n):
    fab = [0] * (n + 1)
    fab[0] = 0
    fab[1] = 1
    for i in range(2, n + 1):
        fab[i] = fab[i - 1] + fab[i - 2]
    return fab[n]
print(fibonacci_ite(5))
print(fibonacci_ite(10))