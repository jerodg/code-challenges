#!/bin/python3

import sys
import os

# Complete the function below.

def  findNumber(arr, k):
    if k in arr:
        return 'YES'
    return 'NO'

	f = open(os.environ['OUTPUT_PATH'], 'w')
    

_arr_cnt = 0
_arr_cnt = int(input())
_arr_i=0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(input());
    _arr.append(_arr_item)
    _arr_i+=1
    


_k = int(input());

res = findNumber(_arr, _k)
f.write(res + "\n")

f.close()