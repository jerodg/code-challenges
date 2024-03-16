#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.07.02

List Operations

If you were to instead utilize full-word commands (insert, remove, append, pop)
this could be written as a one-line comprehension.
"""
import sys
import traceback

if __name__ == '__main__':
    try:
        ls = []

        while 1:  # waiting for input
            cmd = input().split()

            if cmd[0] == 'f':
                ls.insert(0, int(cmd[1]))
            elif cmd[0] == 'i':
                ls.insert(int(cmd[1]), cmd[2])
            elif cmd[0] == 'r':
                try:
                    del ls[0]
                except IndexError:
                    pass
            elif cmd[0] == 'd':
                try:
                    del ls[int(cmd[1])]
                except IndexError:
                    pass
            elif cmd[0] == 'q':
                quit(0)
            else:
                raise NotImplementedError

            if ls:
                print(*ls, sep=' ')
            else:
                print('empty')
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
