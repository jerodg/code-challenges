#!/usr/bin/env python3.6
"""Jerod Gawne, 2017-10-13

Alphabet Rangoli

https://www.hackerrank.com/challenges/alphabet-rangoli

Editorial:
This can be solved using center.

n = int(raw_input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

Sample Input:
5

Sample Output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    """Jerod Gawne, 2017-10-13

    If n is the number of unique letters we will be printing,
    then we end up printing twice this many in any given row.
    We are also printing a '-' for each letter, so now we're
    at 4n characters total. BUT we do no re-print the "middle"
    character, so it and its character are substracted from the
    total. So 4n-2. Now, we also don't want to print the trailing
    '-' so subtract 1 more. Thus, 4n-3 is the width.

    credit: https://www.hackerrank.com/challenges/alphabet-rangoli/forum/comments/208741
    credit: https://www.hackerrank.com/challenges/alphabet-rangoli/forum/comments/254211

    :param size: int
    :return: None
    """
    import string
    alpha = string.ascii_lowercase

    ls = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        ls.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print(*(ls[:0:-1] + ls), sep='\n')


def main():
    """
    Main/Tests
    """
    n = int(input())
    print_rangoli(n)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
