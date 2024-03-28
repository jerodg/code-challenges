'''A little boy is studying arithmetics. He has just learned how to add two integers, written one below another,
column by column. But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.

Note: the boy used this site as the source of knowledge, feel free to check it out too if you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The little boy goes from right to left:

6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the little boy forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the little boy imagines that 0 is
written before 456. Thus, he gets 0 + 1 = 1.
Input/Output

[time limit] 4000ms (py)
[input] integer param1

A non-negative integer.

Constraints:
0 ≤ param1 ≤ 99999.

[input] integer param2

A non-negative integer.

Constraints:
0 ≤ param2 ≤ 59999.

[output] integer

The result that the little boy will get.'''

#!/usr/bin/env python3
""" Add Without Carrying

Copyright ©2023 Jerod Gawne <https://github.com/jerodg/>

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
# def additionWithoutCarrying(param1, param2):
#     temp = 0
#     power = 0
#     # while param1 or param2:
#     temp += ((param1 + param2) % 10) * pow(10, power)
#     param1 /= 10
#     param2 /= 10
#     power += 1
#     return temp

# def solution(param1, param2):
#     return ''.join(str(sum(map(int, x)))[-1] for x in zip(str(param1), str(param2)))

import math


def solution(param1, param2):
    result = 0
    multiplier = 1

    while param1 or param2:
        isum = ((param1 % 10) + (param2 % 10))
        # Neglect carry
        isum %= 10

        # Update result
        result += (isum * multiplier)
        param1 = math.floor(param1 / 10)
        param2 = math.floor(param2 / 10)

        multiplier *= 10

    return result


print(solution(456, 1734))
