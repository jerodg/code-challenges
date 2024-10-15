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
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        next_unsat_chair = 0
        empty_chairs = []
        occupied = []

        for i in range(len(times)):
            times[i].append(i)

        times.sort(key=lambda x: x[0])

        for arrival, leaving, i in times:
            while len(occupied) > 0 and occupied[0][0] <= arrival:
                unsatChair = heapq.heappop(occupied)[1]
                heapq.heappush(empty_chairs, unsatChair)
            if i == targetFriend:
                return empty_chairs[0] if len(empty_chairs) > 0 else next_unsat_chair
            if len(empty_chairs) == 0:
                heapq.heappush(occupied, (leaving, next_unsat_chair))
                next_unsat_chair += 1
            else:
                empty_chair = heapq.heappop(empty_chairs)
                heapq.heappush(occupied, (leaving, empty_chair))
