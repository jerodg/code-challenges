#!/usr/bin/env python3.10
"""Siemens Technical Assessment: Colorized Rooms
Copyright ©2022 Jerod Gawne <https://github.com/jerodg/>

fp0-fp2 are testing iterative complexities
fp3 is testing when the floorplan isn't a square

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
from os import listdir
from os.path import basename, join, realpath
from random import shuffle
from typing import List, NoReturn, Union


def colorize_rooms(floor_plan: List[List[Union[str, int]]]) -> NoReturn:
    """Colorize Rooms

    :param floor_plan: List[List[Union[str, int]]]
    :return: NoReturn"""
    width = len(floor_plan[0])
    count = 0

    # Replace room spaces with a unique number for each
    for i, row in enumerate(floor_plan):
        if ' ' in row:
            for j, col in enumerate(row):
                if col == '#':
                    continue
                elif row[j - 1] == '#' and col == ' ' and row[j + 1] == '#':  # Horizontal Door
                    continue
                elif row[j - 1] == '#' and col == ' ':
                    if floor_plan[i - 1][j] == '#' or floor_plan[i - 1][j] == ' ':  # Check element above

                        floor_plan[i][j] = count
                    else:  # Same room
                        floor_plan[i][j] = floor_plan[i - 1][j]
                elif row[j - 1] != '#' and col == ' ':
                    if floor_plan[i - 1][j] == '#' and floor_plan[i + 1][j] == '#':  # Vertical Door
                        continue
                    elif floor_plan[i - 1][j] != '#' and row[j - 1] == ' ':
                        floor_plan[i][j] = floor_plan[i - 1][j]
                    else:
                        floor_plan[i][j] = row[j - 1]

                    if (j < width - 1) and row[j + 1] == '#':
                        count += 1

    color_codes = [*range(41, 47), *range(100, 107)]  # 8bit terminal background colors
    [shuffle(color_codes) for x in range(5, 25)]  # Randomize the colors so each room gets a different color each iteration

    ephemeral = []
    for row in floor_plan:
        result = []
        for col in row:
            if col not in (' ', '#'):
                if col not in ephemeral:
                    ephemeral.append(col)
                result.append(f'\033[{color_codes[ephemeral.index(col)]}m \033[0m')
            else:
                result.append(col)

        print(''.join(result))


def main():
    floor_plans = [realpath(join('./floor_plans', p)) for p in listdir('./floor_plans')]
    for fp in floor_plans:
        with open(realpath(fp)) as f:
            rows = [list(x.split('\n')[0]) for x in f]

            print(f'--- {basename(fp).split(".")[0]} ---')
            colorize_rooms(rows)
            print('--- end ---\n')


if __name__ == "__main__":
    main()
