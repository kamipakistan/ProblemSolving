"""
# =====================================================================================================
# ======================================== Day 10: Binary Numbers =====================================
# =====================================================================================================
Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

Example
n = 125
The binary representation of 125(base-10) is 1111101(base-2). In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

Input Format
A single integer, n.

Output Format
Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.
"""

# ===================================================================
# ========================= Solution ================================
# ===================================================================

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    # list to store the reminders
    reminder = []
    def Decimal2Binary(n):
        if n > 0:
            # storing the reminder
            reminder.append(n % 2)
            # divide n by 2 and passing again to the funcion
            Decimal2Binary(n // 2)
    
    # calling Decimal2Binary to find the binary number
    Decimal2Binary(n)
    
    # current counts , max number of consecutive ones occure
    count,nConsecutiveOnes = 0,0
    
    # looping through the biary and counting consecutive ones
    for i in reminder:
        # if 0 occure will start the cout from zero
        if i == 0:
            count = 0
        else:
            # if 1 occure will count it.
            count +=1
            nConsecutiveOnes = max(nConsecutiveOnes,count)
            
    print(nConsecutiveOnes)
