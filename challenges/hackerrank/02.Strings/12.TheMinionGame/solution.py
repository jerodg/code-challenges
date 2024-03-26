#!/usr/bin/env python3.7
# coding=utf-8
"""Jerod Gawne, 2018.06.28

https://github.com/jerodg/hackerrank
"""
import sys
import traceback


def minion_game(word="BANANA") -> None:
    """Jerod Gawne, 2018.06.28

    Minion Game

    :param word: str
    :return: None
    """
    vowels = frozenset("AEIOU")
    n = len(word)
    kevin_score = sum(q for c, q in zip(word, range(n, 0, -1)) if c in vowels)
    stuart_score = n * (n + 1) // 2 - kevin_score

    if kevin_score > stuart_score:
        print("Kevin {:d}".format(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart {:d}".format(stuart_score))
    else:
        print("Draw")


if __name__ == "__main__":
    try:
        # minion_game(input())
        minion_game()
    except Exception:
        print(traceback.print_exception(*sys.exc_info()))
