#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-04

Mutations

https://www.hackerrank.com/challenges/python-mutations/

Editorial:
 -
"""


def mutate_string(string, position, character):
    """
    Changes string at position to character

    :param string:
    :param position:
    :param character:
    :return:
    """
    return string[:position] + character + string[position + 1:]


def mutate_string2(string, position, character):
    """
    Changes string at position to character

    :param string:
    :param position:
    :param character:
    :return:
    """
    return ''.join([character if i == position else string[i] for i in range(len(string))])


def main():
    """
    Main/Tests
    """
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
