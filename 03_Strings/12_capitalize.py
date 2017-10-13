#!/usr/bin/env python3.6
"""Jerod Gawne, 2017-10-13

Capitalize

https://www.hackerrank.com/challenges/capitalize

Editorial:
This can be solved using split, join and capitalize.

print ' '.join(word.capitalize() for word in raw_input().split(' '))

Sample Input:
hello world

Sample Output:
Hello World
"""


def capitalize(string):
    """Jerod Gawne, 2017-10-13

    print(input().title()) will not work because the question is
    asking to capitalise firse letter of each word keeping in mind
    that "if it is a letter". Title and Capitalise are different in function as:
    'abcd'.title() results in 'Abcd' but
    '12abcd'.title() results in '12Abcd'. This is not what we want.
    We just want to capitalise first letter of each word, not the first occuring letter of a word.

    credit: https://www.hackerrank.com/challenges/capitalize/forum/comments/99491

    :param string:
    :return:
    """
    return ' '.join((word.capitalize() for word in string.split(' ')))


def main():
    """
    Main/Tests
    """
    print(capitalize(input()))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
