#!/usr/bin/python3.6
"""Jerod Gawne, 2017-09-15

HackkerRank Challenge Lists

https://www.hackerrank.com/challenges/python-lists/

Editorial:
 - We can solve this using list methods and conditionals.

arr = []
for i in range(int(raw_input())):
    s = raw_input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])

    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print arr.index(s[1])
    elif s[0] == "count":
        print arr.count(s[1])
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print arr
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
