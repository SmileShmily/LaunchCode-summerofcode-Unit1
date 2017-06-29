'''Write a function called myPi that will return an approximation of PI (3.14159...). Use the Madhava approximation.
'''

def leibniz_series():
    """Generator producing the Leibniz series (1, -1/3, 1/5, -1/7, ...)."""
    numerator = denominator = 1.0
    while True:
        yield (numerator / denominator)
        numerator *= -1
        denominator += 2

def pi_steps(steps=100):
    """Calculates pi from the Leibniz series with a defined number of steps."""
    values = leibniz_series()
    output = 0
    for _ in range(steps):
        value = 4 * next(values)
        output += value
    return output

def pi_tolerance(tolerance=0.0001):
    """Calculates pi from the Leibniz series with a defined output tolerance."""
    values = leibniz_series()
    output = 0
    value = 4 * next(values)
    while abs(value) > tolerance:
        output += value
        value = 4 * next(values)
    return output
