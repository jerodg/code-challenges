#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        student_marks = {}
        for _ in range(int(input())):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores

        query = input()

        # Not ideal, however, the test interpreter doesn't support hackerrank 3.6+ f-strings
        print("{:0.2f}".format(sum(student_marks[query]) / len(student_marks[query])))
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
