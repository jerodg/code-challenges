#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-02

Finding the Percentage

https://www.hackerrank.com/challenges/finding-the-percentage/

Editorial:
 -Use a dictionary to store the averages as values and the name as keys.

d={}
for i in range(int(raw_input())):
    line=raw_input().split()
    d[line[0]]=sum(map(float,line[1:]))/3

print '%.2f' % d[raw_input()]
"""


def main():
    """
    Main/Tests
    """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    print('{:.2f}'.format(sum(student_marks[query_name]) / len(student_marks[query_name])))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
