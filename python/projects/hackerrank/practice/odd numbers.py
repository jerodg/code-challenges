#!/bin/python3

import os


# Complete the function below.

def oddNumbers(l, r):
    return [i for i in range(l, r + 1, 1) if i % 2 != 0]


f = open(os.environ['OUTPUT_PATH'], 'w')

_l = int(input());

_r = int(input());

res = oddNumbers(_l, _r)
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()

https: // www.sanfoundry.com / python - program - print - odd - numbers - given - range /
lower = int(input("Enter the lower limit for the range:"))
upper = int(input("Enter the upper limit for the range:"))
for i in range(lower, upper + 1):
    if (i % 2 != 0):
        print(i)
Program
Explanation
