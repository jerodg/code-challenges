#!/usr/bin/python3.6
"""Jerod Gawne, 2017-10-05

String Validators

https://www.hackerrank.com/challenges/string-validators/

Editorial:
 -

Sample Input:
qA2

Sample Output:
True
True
True
True
True
"""


def validate(s):
    """Jerod Gawne, 2017-10-05

    :param s:
    :return:
    """
    s = list(s)
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))
    print('\n')


def validate2(s):
    """Jerod Gawne, 2017-10-05

    credit: https://www.hackerrank.com/harishbisht?hr_r=1

    :param s:
    :return:
    """
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
    print('\n')


def validate3(s):
    """Jerod Gawne, 2017-10-05

    Eval should only ever be used with caution;
     - it can lead to malicious code being executed
     - it is slower as it has to be evaluated at every iteration

    credit: https://www.hackerrank.com/yuanster?hr_r=1

    :param s:
    :return:
    """
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for _ in s))
    print('\n')


def validate4(s):
    """Jerod Gawne, 2017-10-05

    credit: https://www.hackerrank.com/itsbruce?hr_r=1

    :param s:
    :return:
    """
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
    print('\n')


def main():
    """
    Main/Tests


    """
    s = input()

    validate(s)
    validate2(s)
    validate3(s)
    validate4(s)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
