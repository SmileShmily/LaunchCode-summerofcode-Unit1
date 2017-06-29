
'''Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.
'''
import turtle
import random
import timeit
import os
import os.path
def hanoi(height,fromPole, toPole, withPole):
    if height >= 1:
        hanoi(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        hanoi(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
       print("moving disk from",fp,"to",tp)
hanoi(3, 'A', 'C', 'B')