#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.18

Write a program that squares an integer and prints the result.
Input:
Your program should read lines from standard input.
Each line will contain a positive integer.

Output:
For each line of input, print to standard output the square of the number.
Print out each result on a search_stax line.
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        print(int(input()) ** 2)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
