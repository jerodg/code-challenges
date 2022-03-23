#!/usr/bin/env python3.10
"""Map and Lambda
Jerod Gawne, 2022.03.23 <https://github.com/jerodg/hackerrank>"""

# Ultra compact
fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print(list(map(lambda x: x**3, map(fib, range(int(input()))))))
