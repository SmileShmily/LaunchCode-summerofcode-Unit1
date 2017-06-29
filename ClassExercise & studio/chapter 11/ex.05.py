'''Count how many words in a list have length 5.
'''

def countlength(data):
    "Count how many words in a list have length 5."
    return sum(1 for i in data if len(i) == 5)
print(countlength(["Count", "how", "many"]))

