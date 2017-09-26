#!/usr/bin/python3.6
"""Jerod Gawne, 2017-06-09

The Coin Change Problem

Given c, input currency

Make change using t, types of coins available in infinite supply

Consider the degenerate cases: 
    How many ways can you make change for 0 cents?
    How many ways can you make change for 0 cents if you have no coins?
"""

import itertools


def bucket(lst, depth=0):
    """ return all combinations of items in buckets """
    # dbg print("of_bucket({0}, {1})".format(lst, depth))
    for item in lst[0]:
        if len(lst) > 1:
            for result in bucket(lst[1:], depth + 1):
                yield [item, ] + result
        else:
            yield [item, ]


def makechange(n, c):
    combos = []
    for n, combination in enumerate(bucket(c)):
        combos.append(combination)
        # print("{0:2d}. {1}".format(n, '-'.join(combination)))
    print(combos)

    # change = []
    # for combo in combos:
    #     if sum(combo) == n:
    #         change.append(combo)
    # print(change)


def equivalent(n, c):
    if sum(c) == n:
        return True
    else:
        return False


def powerset(ls):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(ls)  # allows duplicate elements
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def all_subsets(ss):
    return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(0, len(ss) + 1)))


def getcombos(c):
    combos = []
    l = len(c) + 1
    for i in range(1, l + 1):
        combos += list(itertools.combinations_with_replacement(c, i))
    return combos


def main():
    """ Main Method """
    print(__doc__)

    # n = list(map(int, input().strip().split(' ')))
    # c = list(map(int, input().strip().split(' ')))

    n = 0
    c = [1, 2, 3]

    if n == 0 or len(c) == 0:
        print(1)
    else:
        # makechange(n, c)
        # combos = list(itertools.combinations_with_replacement(c, len(c) + 1))
        combos = getcombos(c)
        # [print(x) for x in combos]
        equiv = [equivalent(n, combo) for combo in combos]
        # print(equiv)
        change = list(itertools.compress(combos, equiv))
        print(len(change))

    # print(sum(combos[0]))
    # equiv = [x for x in combos if sum(x) == n]
    # print('equiv: ', equiv)
    # [print(x) for x in equiv]
    # itertools.compress()
    # for i, combo in enumerate(powerset(c), 1):
    #     # if sum(combo) == n:
    #     print('combo #{}: {}'.format(i, combo))

    # for subset in all_subsets(c):
    #     print(subset)

    # output = sum([map(list, itertools.combinations(c, i)) for i in range(len(c) + 1)], [])
    # print(output)

    # input = ['1', '2', '3']

    # output = sum([itertools.combinations(input, i) for i in range(len(input) + 1)], [])
    # print(output)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import sys
        import traceback

        print(e, traceback.print_exception(*sys.exc_info()))

# n is units or currency total, m is length of array for c
# n, m = input().strip().split(' ')
# n, m = [int(n), int(m)]

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

# Submission
"""
#!/bin/python3

import itertools
import sys

def getcombos(c):
    combos = []
    l = len(c) + 1
    for i in range(1, l + 1):
        combos += list(itertools.combinations_with_replacement(c, i))
    return combos


def equivalent(n, c):
    if sum(c) == n:
        return True
    else:
        return False

def getWays(n, c):
    combos = getcombos(c)
    equiv = [equivalent(n, combo) for combo in combos]
    change = list(itertools.compress(combos, equiv))
    print(len(change))    

    
# n is units or currency total, m is length of array for c
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
"""
