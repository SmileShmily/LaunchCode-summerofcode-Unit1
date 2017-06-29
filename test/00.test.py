n1 = "Hello"
n2 = "abc"
n3 = "i'm lovin this test"
n4 = "i'm not kidding"
n5 = "exclamation points are not really my up of tea"
# Your function here!
def string_function(s):
    return s + '!'
print (string_function(n1))
print (string_function(n2))
print (string_function(n3))
print (string_function(n4))
print (string_function(n5))


#list=["Hello","abc","i'm lovin this test","i'm not kidding","exclamation points are not really my up of tea"]
def printlist(a):
    for i in a:
        if type(i) is list:
            printlist(i)
        else:
            print(i+"!")
t=["Hello","abc","i'm lovin this test","i'm not kidding","exclamation points are not really my up of tea"]

printlist(t)



def number(n):
    count = 0
    while count < 10: # Add a colon
        print (count)
    # Increment count
        count += 1
print(number(8))





def digit_sum(n):
    b = []
    n = str(n)
    for a in n:
        a = int(a)
        b.append(a)
    return sum(b)
    print(sum(b))
