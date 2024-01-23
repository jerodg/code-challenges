#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.18

https://github.com/jerodg/hackerrank
"""
import sys
import traceback

if __name__ == "__main__":
    try:
        l = []
        for _ in range(int(input())):
            s = input().split()
            cmd = s[0]
            args = s[1:]
            if cmd != "print":
                cmd += "(" + ",".join(args) + ")"
                eval("l." + cmd)
            else:
                print(l)
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
