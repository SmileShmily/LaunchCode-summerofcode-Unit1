""" Work out Pascal's triangle into a list of
lists ... """

tri =[]

for row in range(12):
   for col in range(row+1):
      if col == 0:
         tri.append([1])
      elif col == row:
         tri[row].append(1)
      else:
         tri[row].append(tri[row-1][col]+tri[row-1][col-1])

for row in tri:
   nvals = len(row)
   spaces = (80 - 5 * nvals)/2
   paddington = " " * spaces
   bear = ""
   for val in row:
      bear += "%5x" % val
   print (paddington + bear)