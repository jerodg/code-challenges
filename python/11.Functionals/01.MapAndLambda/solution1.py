#!/usr/bin/env python3.10
"""Map and Lambda
Jerod Gawne, 2022.03.23 <https://github.com/jerodg/hackerrank>"""

cube = lambda x: x ** 3


# Use dynamic programming via generator to save memory
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
