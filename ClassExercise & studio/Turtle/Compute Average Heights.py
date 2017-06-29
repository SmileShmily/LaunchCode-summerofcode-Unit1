# This is a simple program to compute average heights.
# It prompts user for heights, sums them, and divides by the number of heights.
# Exit is signalled by negative height. There are (at least) 2 errors. Find and fix!


sum = 0.0
num = 0
done = False

while not done:

    height = float(input("Enter a height or 0: "))

    if height < 0:

        done = True

    else:

        sum += height
        num += 1

print("Average height is ", sum / num)