#!/usr/bin/env python3.9
"""Deduplicate Matched Pairs

Finds the union of two sets, deduplicated by matched pairs,
    with leftovers intact, and ignoring order.

Jerod Gawne, 2021.09.21 <https://github.com/jerodg>"""
import time

LIST0 = ['orange', 'apple', 3, 'orange']
LIST1 = ['apple', 'orange', 'watermelon', 5]
RESULT = ['orange', 3, 'watermelon', 5]


def mixed(num: int) -> tuple:
    """Key for a mixed data-types sort.

    A helper function for testing.

        Args:
        num (int):

    Returns:
        (tuple)"""
    try:
        ele = int(num)
        return 0, ele, ''
    except ValueError:
        return 1, num, ''


def compare(a: list, b: list) -> bool:
    """Compare two lists to see if they are the same while ignoring order.

    A helper function for testing.

    Args:
        a (list):
        b (list):

    Returns:
        (bool)"""
    if (len(a) == len(b)) and (all(i in b for i in a)):
        return True

    return False


def sym(a: list, b: list) -> list:
    if len(a) > len(b):
        for x in a:
            if x in b:
                a.remove(x)
                b.remove(x)
    else:
        for x in b:
            if x in a:
                a.remove(x)
                b.remove(x)

    return list(set(a).union(set(b)))


def test_sym():
    ts = time.perf_counter()

    result = sym(LIST0, LIST1)
    print('\nresult:', result)

    assert compare(result, RESULT)

    result.sort(key=mixed)
    RESULT.sort(key=mixed)
    assert result == RESULT

    print(f'Completed in {(time.perf_counter() - ts):f} seconds.')
