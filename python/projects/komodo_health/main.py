# We have a slow performing sum function that gets called multiple times during a process. Implement a cache so that the result
# of identical inputs can be retrieved from memory.

# Feel free to use the Collections library. Otherwise, stick to standard Python data types and structures.

# use this as an example of a slow performing function

from functools import wraps
from time import sleep
from typing import List

CACHE = dict()


def cache(f, size=2):
    @wraps(f)
    def wrapper(args):
        c = CACHE.keys()
        print(c)
        if len(c) > 2:
            del CACHE[c[-1]]

        # CACHE = {k: v for k, v in c}

        # print('args:', args)
        k = ''.join([str(x) for x in sorted(args)])

        # print('args:', args)
        if CACHE.get(k):
            return CACHE[k]
        else:
            CACHE[k] = f(args)
            return CACHE[k]

    return wrapper


@cache
def slow_sum(vals: List[int]) -> int:
    sleep(1)
    return sum(vals)


test_vals = [[1, 2], [2, 1], [3, 3], [3, 3], [9, 0], [0, 9], [1, 2, 3, 3], [2, 1]]
# print(test_vals[0])
# for x in test_vals:
#     print(slow_sum(x))

[print(slow_sum(x)) for x in test_vals]
