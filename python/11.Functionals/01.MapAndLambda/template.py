#!/usr/bin/env python3
from typing import Union


def can_construct(num: str, array: str, memo: dict) -> Union[bool, str, int]:
    if num in memo:
        return memo[num]

    if not num:
        return 1

    count = 0
    for st in array:
        if num.startswith(st):
            size = len(st)
            if can_construct(num[size::], array, memo) == 1:
                count += 1
                memo[num] = True
                return memo[num]

    memo[num] = False

    return False


def integer_convert(array: str) -> str:
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_cache = {'zero': 0, 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0, 'seven': 0, 'eight': 0, 'nine': 0}
    numbers_ref = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for num in numbers:
        if can_construct(num, array, dict()):
            for char in num:
                array.replace(char, '', 1)
            numbers_cache[num] += 1

    print(numbers_cache)

    result = ''
    for key, value in numbers_cache.items():
        result += (str(numbers_ref[key]) * value)

    return result


if __name__ == '__main__':
    print(integer_convert('oneninetwoninenine'))
