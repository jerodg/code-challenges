#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-15

HackkerRank

https://www.hackerrank.com/challenges/python-lists/
"""


def main():
    """
    Main/Tests
    """
    q = [input().split() for _ in range(int(input()))]

    ls = []
    for i in q:
        if i[0] == 'insert':
            ls.insert(int(i[1]), int(i[2]))
        elif i[0] == 'remove':
            ls.remove(int(i[1]))
        elif i[0] == 'append':
            ls.append(int(i[1]))
        elif i[0] == 'sort':
            ls.sort()
        elif i[0] == 'print':
            print(ls)
        elif i[0] == 'pop':
            ls.pop()
        elif i[0] == 'reverse':
            ls.reverse()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
