#!/bin/python3
"""
Sample Input
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""
import os
from datetime import datetime

tme_fmt = '%a %d %b %Y %H:%M:%S %z'


# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(int((datetime.strptime(t1, tme_fmt) - datetime.strptime(t2, tme_fmt)).total_seconds()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
