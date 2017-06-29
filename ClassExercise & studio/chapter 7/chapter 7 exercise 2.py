'''Write a function print_triangular_numbers(n) that prints out the first n triangular numbers.
A call to print_triangular_numbers(5) would produce the following output:

1       1
2       3
3       6
4       10
5       15

'''

def formula(n):
    ith_sum = 0
    for i in range(1, n+1):
        ith_sum += i
        print (i, '\t', ith_sum)
print(formula(5))