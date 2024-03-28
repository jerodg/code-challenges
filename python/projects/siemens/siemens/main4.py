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
import numpy as np
from colored import bg
from os.path import realpath
from random import randint
from rich import print as rprint


# Python program to find all
# rectangles filled with 0


def findend(i, j, a, output, index):
    x = len(a)
    y = len(a[0])

    # flag to check column edge case,
    # initializing with 0
    flagc = 0

    # flag to check row edge case,
    # initializing with 0
    flagr = 0

    for m in range(i, x):

        # loop breaks where first 1 encounters
        if a[m][j] == 1:
            flagr = 1  # set the flag
            break

        # pass because already processed
        if a[m][j] == 5:
            pass

        for n in range(j, y):

            # loop breaks where first 1 encounters
            if a[m][n] == 1:
                flagc = 1  # set the flag
                break

            # fill rectangle elements with any
            # number so that we can exclude
            # next time
            a[m][n] = 5

    if flagr == 1:
        output[index].append(m - 1)
    else:
        # when end point touch the boundary
        output[index].append(m)

    if flagc == 1:
        output[index].append(n - 1)
    else:
        # when end point touch the boundary
        output[index].append(n)


def get_rectangle_coordinates(a):
    # retrieving the column size of array
    size_of_array = len(a)

    # output array where we are going
    # to store our output
    output = []

    # It will be used for storing start
    # and end location in the same index
    index = -1

    for i in range(0, size_of_array):
        for j in range(0, len(a[0])):
            if a[i][j] == 0:
                # storing initial position
                # of rectangle
                output.append([i, j])

                # will be used for the
                # last position
                index = index + 1
                findend(i, j, a, output, index)

    # for o in output:
    #     output[2] += 1
    #     rprint(o)

    return output


def doOverlap(l1, r1, l2, r2):
    # To check if either rectangle is actually a line
    # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}

    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        # the line cannot have positive overlap
        return False

    # If one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    # If one rectangle is above other
    if (r1.y >= l2.y or r2.y >= l1.y):
        return False

    return True


with open(realpath('input.txt')) as f:
    rows = [list(x.split('\n')[0]) for x in f]

# orig = rows.copy()
fp = np.array(rows)
# print(*fp, sep='\n')
# Replace with 0s & 1s
for row in rows:
    for i, col in enumerate(row):
        if col == '#':
            row[i] = 1
        elif col == ' ':
            row[i] = 0
rprint(rows)
rws = rows.copy()
rprint(rws)
# x = bg(randint(18, 231))
# print(f'{x}        ')
rooms = get_rectangle_coordinates(rws)
rprint(rows)
rprint(rooms)
# print(type(rows))
# for i, r in enumerate(rooms):
#     # x = room[:2]
#     # y = room[2:]
#     # r = np.array(fp[room])
#     # print('r:', r)
#     print(fp[np.ix_(r[0],r[1],[r[2], r[3]])])
# print(*rooms, sep='\n')
# rprint(rooms)

# r = rooms[0]
# print(r)
# print(
#
#         # fp[1:3, 1:4]
# )

# rprint(fp)
# for row in fp:
#     rprint(''.join(row))
# print(fp.size)
# for r in rooms:
#
#     # room = fp[r[0]:r[2] + 1, r[1]:r[3] + 1:1]
#     # if room.size >= 4:
#     fp[r[0]:r[2], r[1]:r[3]] = 'r'

    # print('size:', np.size(room))
    # if np.size(room) >= 4:
    #     room = '0'
# rprint(fp)
rprint(rows)
# for r in rooms:
#     x = fp[r[0],r[1]:r[2],r[3]]
#     print(x)
#
# for x in fp:
#     print(''.join(x))

# for room in rooms:
#     x = room[:2]
#     y = room[2:]
#     print(f'x: {x[0], x[1]}, y: {y[0], y[1]}')
#     # fp[x[0]-1:x[1]-1, y[0]-1:y[1]-1] = 0
#     fp[x[0]:x[1], y[0]:y[1]] = 0
# print(fp)
#
# for x in fp.tolist():
#     print(''.join(x))
