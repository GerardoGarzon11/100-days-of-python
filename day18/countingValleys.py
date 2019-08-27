#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # > 0 = above sea level
    # 0 = sea level,
    # < 0 below sea level
    height = 0 
    in_valley = False

    valleys = 0

    for step in s:
        height += 1 if step == 'U' else -1

        if height == 0 and in_valley == True:
            valleys += 1
            in_valley = False
        elif height < 0 and in_valley == False:
            in_valley = True

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # number of steps
    n = int(input())

    # path description (U's and S's)
    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
