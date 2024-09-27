"""Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""

import bisect


class MyCalendarTwo:
    """A class to manage booking events in a calendar with double booking allowed.

    This class allows booking events in a calendar where each event can be booked at most twice.
    It uses two lists to keep track of single and double bookings and ensures that no event is
    booked more than twice.

    Attributes:
        single_booked (list[int]): A list to store intervals that are booked once.
        double_booked (list[int]): A list to store intervals that are booked twice.
    """

    def __init__(self):
        """Initialize the MyCalendarTwo class with empty booking lists."""
        self.single_booked = []
        self.double_booked = []

    def intersection(self, intervals: list[int], s: int, e: int) -> list[int]:
        """Find the intersection of a given interval with existing intervals.

        This method finds the overlapping intervals between the given interval [s, e) and the
        intervals in the provided list. It uses binary search to efficiently find the relevant
        intervals.

        Parameters:
            intervals (list[int]): The list of existing intervals.
            s (int): The start of the new interval.
            e (int): The end of the new interval.

        Returns:
            list[int]: A list of intervals that intersect with the given interval.
        """
        l = bisect.bisect_left(intervals, s)
        r = bisect.bisect_right(intervals, e)

        intersection = []

        if l % 2:
            # If the start of the new interval is within an existing interval
            if intervals[l] != s:
                intersection.append(s)
            else:
                l += 1

        intersection += intervals[l:r]

        if r % 2:
            # If the end of the new interval is within an existing interval
            if intervals[r - 1] != e:
                intersection.append(e)
            else:
                intersection.pop()

        return intersection

    def add(self, intervals: list[int], s: int, e: int):
        """Add a new interval to the list of intervals.

        This method adds a new interval [s, e) to the provided list of intervals, ensuring that
        the list remains sorted and non-overlapping.

        Parameters:
            intervals (list[int]): The list of existing intervals.
            s (int): The start of the new interval.
            e (int): The end of the new interval.
        """
        l = bisect.bisect_left(intervals, s)
        r = bisect.bisect_right(intervals, e)

        new = []
        if not l % 2:
            new.append(s)

        if not r % 2:
            new.append(e)

        intervals[l:r] = new

    def book(self, start: int, end: int) -> bool:
        """Book a new event in the calendar.

        This method attempts to book a new event in the calendar. It checks for intersections with
        existing double bookings to ensure no event is booked more than twice. If the booking is
        valid, it updates the single and double booking lists accordingly.

        Parameters:
            start (int): The start time of the new event.
            end (int): The end time of the new event.

        Returns:
            bool: True if the booking is successful, False otherwise.
        """
        if self.intersection(self.double_booked, start, end):
            return False

        intersection = self.intersection(self.single_booked, start, end)

        if intersection:
            for i in range(len(intersection) // 2):
                i1 = intersection[2 * i]
                i2 = intersection[2 * i + 1]
                self.add(self.double_booked, i1, i2)

        self.add(self.single_booked, start, end)

        return True
