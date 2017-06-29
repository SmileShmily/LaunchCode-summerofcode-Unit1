def sum_even_lol(lol):
    return sum(n for l in lol for n in l if not n % 2)
print(sum_even_lol([[1,2,3],[6,5,4],[5,7,9]]))


'''or if you find nested generators less readable than ideal, you can reduce by using sum() - but you have to remember to provide an empty array as the initial value:

    return sum(n for n in sum(lol, []) if not n % 2)'''