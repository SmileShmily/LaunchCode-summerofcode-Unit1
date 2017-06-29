'''Find or invent an algorithm for drawing a fractal mountain. Hint: One approach to this uses triangles again.
'''

def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
print(fibonacci_rec(5))
print(fibonacci_rec(10))