'''Count how many words occur in a list up to and including the first occurrence of the word “sam”.
'''

def countinclude(data, s="sam"):
    """Count how many words occur in a list up to and including the first
    occurrence of the word "sam"."""
    count = 0
    for i in data:
        count += 1
        if i == s:
            break
    return count