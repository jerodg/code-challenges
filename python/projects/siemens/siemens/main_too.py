#!/usr/bin/env python3.10
"""Siemens Technical Assessment: Colorized Rooms
Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>

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
# import numpy as np
from devtools import debug
from os.path import realpath
from rich.console import Console

c = Console(color_system='256')

VT = '║'

VTLR = '╣'

VTRR = '╠'

HLCU = '╩'

HLCD = '╦ '

HR = '═'

CRS = '╬'

DRH = '/'

DRV = '/'

BL = '╚'
TL = '╔'
BR = '╝'
TR = '╗'

# Ideally a machine learning algorithm would work best to automatically classify points
checks = {
        'TL':   [[' ', ' ', ' '],
                 [' ', '#', '#'],
                 [' ', '#', ' ']],

        'TR':   [[' ', ' ', ' '],
                 ['#', '#', ' '],
                 [' ', '#', ' ']],

        'BR':   [[' ', '#', ' '],
                 ['#', '#', ' '],
                 [' ', ' ', ' ']],

        'BL':   [[' ', '#', ' '],
                 [' ', '#', '#'],
                 [' ', ' ', ' ']],

        'VT':   [[' ', '#', ' '],
                 [' ', '#', ' '],
                 [' ', '#', ' ']],  # needs work

        'HR':   [[' ', ' ', ' '],
                 ['#', '#', '#'],
                 [' ', ' ', ' ']],

        'VTLR': [[' ', '#', ' '],
                 ['#', '#', ' '],
                 [' ', '#', ' ']],

        'VTRR': [[' ', '#', ' '],
                 [' ', '#', '#'],
                 [' ', '#', ' ']],

        'HLCU': [[' ', '#', ' '],
                 ['#', '#', '#'],
                 [' ', ' ', ' ']],

        'HLCD': [[' ', ' ', ' '],
                 ['#', '#', '#'],
                 [' ', '#', ' ']],

        'CRS':  [[' ', '#', ' '],
                 ['#', '#', '#'],
                 [' ', '#', ' ']],

        'DRH':  [[' ', ' ', ' '],
                 ['#', ' ', '#'],
                 [' ', ' ', ' ']],

        'DRV':  [[' ', '#', ' '],
                 [' ', ' ', ' '],
                 ['#', '#', '#']]
}


# def cos_sim_2d(x, y):
#     norm_x = x / np.linalg.norm(x, axis=1, keepdims=True)
#     norm_y = y / np.linalg.norm(y, axis=1, keepdims=True)
#     return np.matmul(norm_x, norm_y.T)


# def pre_parse(inpt: np.array) -> np.array:
#     res = np.copy(inpt)
#     # rbnds = len(inpt) - 2
#     # cbnds = len(inpt[0]) - 2
#     # debug(rbnds)
#     # debug(cbnds)
#     # print(*inpt, sep='\n')
#     # print('len_input', len(inpt), len(inpt[0]))
#     # xcnt = 0
#     # ycnt = 0
#     debug(inpt)
#     debug(res)
#
#     for i, row in enumerate(inpt[1:]):
#         print(f'i: {i}, row: "{row}"')
#         # if i <= len(inpt):
#         for j, col in enumerate(row[1:]):
#             print(f'j: {j}, col: "{col}"')
#
#             point = [
#                     [inpt[i - 1][j - 1], inpt[i - 1][j], inpt[i - 1][j + 1]],
#                     [inpt[i][j - 1], inpt[i][j], inpt[i][j + 1]],
#                     [inpt[i + 1][j - 1], inpt[i + 1][j], inpt[i + 1][j + 1]]])
#             debug(point)
#             match = next((k for k, v in checks.items() if np.array_equal(point, v)), None)
#
#             for k, v in checks.items():
#                 print(cos_sim_2d(point, v))
#
#             if match:
#                 for k, v in checks.items():
#                     print(cos_sim_2d(point, v))
#
#
#                 quit()
#                 debug(match)
#                 debug(globals().get(match))
#                 res[i][j] = globals().get(match)
#     debug(res)
#                 #
#                 # if not match:
#                 #     # print('Does not match:')
#                 #     # debug(point)
#                 #     pass
#                 # else:
#                 #     print('Matches:')
#                 #
#                 #     # debug(point)
#                 #     debug(match)
#                 #     debug(point)
#                 #     # print(globals().get(match))
#                 #     res[x][y] = globals().get(match) or ' '
#                 #     # checks[match][x][y]
#                 # # print(res)
#                 # # quit()
#
#     [print(''.join(row)) for row in res]


def main():
    # Get the floorplan
    with open(realpath('input.txt')) as f:
        rows = [list(x.split('\n')[0]) for x in f]

    print(*rows, sep='\n')

    while i, row := enumerate(rows):
        pass

    for i, row in enumerate(rows):
        for j, col in enumerate(row):




    chk = {

    }
    for k, v in checks.items():
        # print('k:', k)
        # print('v:', v)
        # out = ''
        # for x in v:
        #     out += ''.join(x)
            # out += '\n'
        # out = ''.join([''.join(item) for row in v[0] for item in row])
        # print('-'*3)
        # print(out)
        # print('-' * 3)
        # out = [''.join([x for x in k])]
        # out = list(zip(v[0][0], v[0][1], v[0][2]))
        # out = ''.join()
        out = ''
        for x in v:
            out += f'{"".join(x)}\n'
            # print('x:', x)
        chk[k] = out
        # print(out)

        # debug(chk)
        # for k, v in chk.items():
        #     print('-'*3)
        #     print(v)
        #     print('-' * 3, '\n')
        # debug(out)
    #
    #     # Pad the floorplan to prevent out of bounds exceptions and make matching easier
    #     rows.insert(0, [' ' for x in range(len(rows[0]))])
    #     rows.append([' ' for x in range(len(rows[0]))])
    #     for row in rows:
    #         row.insert(0, ' ')
    #         row.append(' ')
    #
    # test = rows)
    # debug(test)
    # pre_parse(rows))
    # print(globals().get('BR'))

    # x = [[' ', '#', ' '],
    #               ['#', '#', ' '],
    #               [' ', ' ', ' ']])

    # x = [[' ', ' ', ' '],
    #               ['#', '#', ' '],
    #               [' ', '#', ' ']])
    # y = next((v for k, v in checks.items() if np.array_equal(x, v)), None)
    # print(y)


if __name__ == '__main__':
    main()
