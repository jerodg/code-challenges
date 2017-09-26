#!/usr/bin/python3.6
"""
Jerod Gawne, 2017-09-12

HackkerRank

https://www.hackerrank.com/challenges/decorators-2-name-directory
"""


def person_lister(f):
    """

    :param f:
    :return:
    """
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


def main():
    """
    Main-Logic
    """
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        import sys
        import traceback

        print(traceback.print_exception(*sys.exc_info()))
