'''One thing that you might note about this example matrix is that there are many items that are zero.
In fact, only three of the data values are nonzero. This type of matrix has a special name. It is called a sparse matrix.

Since there is really no need to store all of the zeros, the list of lists representation is considered to be inefficient.
 An alternative representation is to use a dictionary. For the keys, we can use tuples that contain the row and column numbers.
  Here is the dictionary representation of the same matrix.

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

We only need three key-value pairs, one for each nonzero element of the matrix. Each key is a tuple, and each value is an integer.

To access an element of the matrix, we could use the [] operator:

matrix[(0, 3)]

Notice that the syntax for the dictionary representation is not the same as the syntax for the nested list representation.
Instead of two integer indices, we use one index, which is a tuple of integers.

There is one problem. If we specify an element that is zero, we get an error, because there is no entry in the dictionary with that key.
The alternative version of the get method solves this problem. The first argument will be the key.
The second argument is the value get should return if the key is not in the dictionary (which would be 0 since it is sparse).
'''

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix.get((0,3)))

print(matrix.get((1, 3), 0))
