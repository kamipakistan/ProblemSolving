#!/bin/python3

import math
import os
import random
import re
import sys

# Checking if the code is being run as the main program
if __name__ == '__main__':
    # Getting input from user and converting it to an integer
    n = int(input().strip())

    # Checking if n is odd
    if n%2 ==1:
        print("Weird")
    else:
        # Checking if n is between 2 and 6 (inclusive)
        if 2<n<6:
            print("Not Weird")
        # Checking if n is between 6 and 20 (inclusive)
        elif 5<n<21:
            print("Weird")
        # Checking if n is greater than 20
        elif n > 21:
            print('Not Weird')
        else:
            # If none of the above conditions are met, then the input is wrong
            print("Wrong Input")
