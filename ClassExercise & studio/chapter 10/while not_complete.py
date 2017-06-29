'''Each time around the while not_complete loop, you make a pass over the whole of the sequence.
 But there is an easy optimization, noted by Wikipedia:

    The bubble sort algorithm can be easily optimized by observing that the n-th pass finds the n-th largest element and puts it into its final place.
     So, the inner loop can avoid looking at the last n-1 items when running for the n-th time.
'''
def bubble_sort(seq):
    """Sort the mutable sequence seq in place and return it."""
    for i in reversed(range(len(seq))):
        finished = True
        for j in range(i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                finished = False
        if finished:
            break
    return seq