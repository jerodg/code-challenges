"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Codewars Kata: Test Sum of Pairs
"""
# todo: failing tests
import time

from code_wars.sum_of_pairs import sum_pairs


def test_basic_examples() -> None:
    """Test the examples given in the kata description."""
    assert sum_pairs([11, 3, 7, 5], 10) == [3, 7]
    assert sum_pairs([4, 3, 2, 3, 4], 6) == [4, 2]
    assert sum_pairs([0, 0, -2, 3], 2) is None
    assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]


def test_empty_and_single_element_lists() -> None:
    """Test edge cases with empty list and single element list."""
    assert sum_pairs([], 10) is None
    assert sum_pairs([5], 5) is None
    assert sum_pairs([5], 10) is None


def test_no_pairs_sum_to_target() -> None:
    """Test when no pairs in the list sum to the target value."""
    assert sum_pairs([1, 2, 3, 4, 5], 20) is None
    assert sum_pairs([-1, -2, -3], 0) is None


def test_multiple_valid_pairs() -> None:
    """Test when multiple pairs sum to the target, ensuring we get the pair with earliest second element."""
    assert sum_pairs([1, 4, 8, 7, 3, 15], 8) == [1, 7]
    assert sum_pairs([1, -2, 3, 0, -6, 1], -6) == [0, -6]


def test_duplicate_numbers() -> None:
    """Test with duplicate numbers in the list."""
    assert sum_pairs([5, 9, 13, -3, 5, 1], 10) == [5, 5]
    assert sum_pairs([6, 6, 6, 6, 6], 12) == [6, 6]


def test_negative_numbers() -> None:
    """Test with negative numbers in the list."""
    assert sum_pairs([-10, -8, -12, 20, 15], 10) == [-10, 20]
    assert sum_pairs([-1, -5, -10, -15, 20], 5) == [-15, 20]


def test_performance() -> None:
    """Test performance with a larger list to ensure the solution is efficient."""
    # Create a large list where the solution is near the end
    large_list = [*list(range(100000)), 5000, 10000]
    start_time = time.time()
    result = sum_pairs(large_list, 15000)
    end_time = time.time()

    assert result == [5000, 10000]
    # Ensure it completes within a reasonable time (less than 1 second)
    assert end_time - start_time < 1
