myList = [43, 21, 12, 80, 3, 2, 35]
end = len(myList) - 1
while (end != -1):
    swapped = -1
    for i in range(0, end):
        if myList[i] > myList[i + 1]:
            temp = myList[i]
            myList[i] = myList[i + 1]
            myList[i + 1] = temp
            swapped = i
    end = swapped
print(myList)