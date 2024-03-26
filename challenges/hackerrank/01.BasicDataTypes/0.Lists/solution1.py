#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        q = [input().split() for _ in range(int(input()))]

        ls = []
        for i in q:
            if i[0] == "insert":
                ls.insert(int(i[1]), int(i[2]))
            elif i[0] == "remove":
                ls.remove(int(i[1]))
            elif i[0] == "append":
                ls.append(int(i[1]))
            elif i[0] == "sort":
                ls.sort()
            elif i[0] == "print":
                print(ls)
            elif i[0] == "pop":
                ls.pop()
            elif i[0] == "reverse":
                ls.reverse()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
