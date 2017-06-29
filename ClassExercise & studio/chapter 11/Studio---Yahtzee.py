'''In this studio, we simulate the game of Yahtzee.
The program asks the user for the number of die they roll and the number of times the dice are thrown.
 The rollDice function is given to you. You must create the sumOfRoll function.
 If you finish that, you move on to the bonus function, Yahtzee.
'''
import random
#from test import testEqual

# The rollDice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the array.

def rollDice(dice, rolls):
    double_array = [[0 for i in range((int)(dice))] for j in range((int)(rolls))]
    for i in range(0, len(double_array)):
        for j in range(0, len(double_array[i])):
            double_array[i][j] = (int)(random.random()*6 + 1)
    return double_array

# This function takes a 2D array (which can be generated by rollDice)
# and sums the value of all the dice in each row. It returns a 1
# dimensional array with the sum of each throw.
# Example:
# double_array: [[1, 5, 6],[2, 3, 1],[1, 3, 3]]
# sumOfRoll should return: [12, 6, 7]
'''
def sumOfRoll(double_array):
   '# return max([len(group) for group in range(double_array)]) == 3 and sum(double_array) or 0
    score = 0
    for i in double_array:
        if dice.count(i) >= 3:
            score = sum(double_array)
            return score
        else:
            return score
            '''


def sumOfRoll(double_array):
    SoR = []
    for a in double_array:
        sub = 0
        for x in range(0, len(a)):
            sub = sub + a[x]
        SoR.append(sub)
    return SoR


# Bonus function! Takes a 2 dimensional array and returns
# the number of times a person rolls Yahtzee (all dice have
# the same value). Hint: you may want to create a helper
# function that takes individual rows of the array.

def yahtzee(double_array):
    return 50 if len(double_array) == 5 and len(set(double_array)) == 1 else 0





dice = input("How many dice?")
rolls = input("What is the number of rolls?")

array = rollDice(dice, rolls)
print("Testing sumOfRoll...")
testEqual(sumOfRoll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
testEqual(sumOfRoll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
testEqual(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
testEqual(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)


