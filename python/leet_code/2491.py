"""Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
"""


class Solution:
    """
    A class used to represent the solution to the problem of dividing players into pairs based on their skill levels.
    """

    def dividePlayers(self, skill: List[int]) -> int:
        """
        Divides players into pairs such that the sum of skills in each pair is the same and returns the sum of the
        product of skills in each pair.

        Args:
            skill (List[int]): A list of integers representing the skill levels of the players.

        Returns:
            int: The sum of the product of skills in each pair if possible, otherwise -1.
        """
        sum_ = sum(skill)
        n = len(skill)

        # If there are only two players, return the product of their skills.
        if n == 2:
            return skill[0] * skill[1]

        # If the total sum of skills is not divisible by the number of pairs, return -1.
        if sum_ % (n // 2) != 0:
            return -1

        skill.sort()
        score = skill[0] + skill[-1]
        result = 0

        # Iterate through the first half of the sorted skill list to form pairs.
        for i in range(n // 2):
            l, r = skill[i], skill[n - 1 - i]

            # If the sum of the current pair does not match the expected score, return -1.
            if l + r != score:
                return -1

            # Accumulate the product of the current pair's skills.
            result += l * r

        return result


with open("user.out", "w") as f:
    inputs = map(loads, stdin)

    # Process each input and write the result to the output file.
    for nums in inputs:
        print(Solution().dividePlayers(nums), file=f)

exit(0)
