#!/usr/bin/env python3
"""Regex Substitution

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""

from re import compile, sub

re_and = compile(r'(?<=\s)&{2}(?=\s)')
re_or = compile(r'(?<=\s)\|{2}(?=\s)')


def main():
    i = int(input())

    lines = []
    for j in range(i):
        line = input()
        x = sub(re_and, 'and', line)
        y = sub(re_or, 'or', x)
        lines.append(y)

    print(*lines, sep='\n')


if __name__ == '__main__':
    main()
