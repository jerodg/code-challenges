#!/usr/bin/python3.6
"""Jerod Gawne, 2017-09-28

Find the Second Largest Number

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

Editorial:
 - There are many ways to solve this problem.
   This can be solved by maintaining two variables max and second_max.
   Iterate through the list and find the maximum and store it.
   Iterate again and find the next maximum value by having an if
   condition that checks if it's not equal to first maximum.
   Create a counter from the given array. Extract the keys, sort them
   and print the second last element.
   Transform the list to a set and then list again, removing all the
   duplicates. Then sort the list and print the second last element.
"""


def main():
    """
    Main/Tests
    """
    input()
    print(sorted(set(map(int, input().split())))[-2])


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
