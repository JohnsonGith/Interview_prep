#!/bin/python3

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        segment_sum = sum(s[i:i + m])
        if segment_sum == d:
            count += 1
    return count
    for i in range(len(s) - m + 1):
        segment_sum = sum(s[i:i + m])
        if segment_sum == d:
            count += 1
    return count
    