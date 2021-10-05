#!/usr/bin/env python3.9
"""Number Replacement
Jerod Gawne, 2021.09.15 <https://github.com/jerodg>"""

NUMBERS = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def main():
    inpt = 'oneninetwoninenine'

    for k, v in NUMBERS.items():
        if k in inpt:
            inpt = inpt.replace(k, v)

    print(inpt)


if __name__ == '__main__':
    main()
