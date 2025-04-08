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
"""

import unittest

import pytest
from lists import (
    approx_average_is_average,
    average_even_is_average_odd,
    card_average,
    concatenate_rounds,
    get_rounds,
    list_contains_round,
    maybe_double_last,
)


class CardGamesTest(unittest.TestCase):
    """Test suite for card games functions.

    This test class verifies the functionality of various card game operations,
    including round handling, list operations, and card value calculations.
    """

    @pytest.mark.task(taskno=1)
    def test_get_rounds(self) -> None:
        """Test that get_rounds returns the current round and next two rounds.

        Verifies that the function returns a list containing the given round number
        and the next two consecutive round numbers.
        """
        input_data = [0, 1, 10, 27, 99, 666]
        result_data = [[0, 1, 2], [1, 2, 3], [10, 11, 12], [27, 28, 29], [99, 100, 101], [666, 667, 668]]

        for variant, (number, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", number=number, expected=expected):
                actual_result = get_rounds(number)
                error_message = (
                    f"Called get_rounds({number}). "
                    f"The function returned {actual_result}, "
                    f"but the tests expected rounds {expected} "
                    f"given the current round {number}."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_concatenate_rounds(self) -> None:
        """Test that concatenate_rounds joins two lists of round numbers.

        Verifies that the function combines two lists, preserving the order
        of elements from both input lists.
        """
        input_data = [([], []), ([0, 1], []), ([], [1, 2]), ([1], [2]), ([27, 28, 29], [35, 36]), ([1, 2, 3], [4, 5, 6])]

        result_data = [[], [0, 1], [1, 2], [1, 2], [27, 28, 29, 35, 36], [1, 2, 3, 4, 5, 6]]

        for variant, ((rounds_1, rounds_2), expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", rounds_1=rounds_1, rounds_2=rounds_2, expected=expected):
                actual_result = concatenate_rounds(rounds_1, rounds_2)
                error_message = (
                    f"Called concatenate_rounds({rounds_1}, {rounds_2}). "
                    f"The function returned {actual_result}, but the tests "
                    f"expected {expected} as the concatenation "
                    f"of {rounds_1} and {rounds_2}."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_list_contains_round(self) -> None:
        """Test that list_contains_round correctly checks for round presence.

        Verifies that the function returns True when the specified round number
        is present in the list and False otherwise.
        """
        input_data = [([], 1), ([1, 2, 3], 0), ([27, 28, 29, 35, 36], 30), ([1], 1), ([1, 2, 3], 1), ([27, 28, 29, 35, 36], 29)]
        result_data = [False, False, False, True, True, True]

        for variant, ((rounds, round_number), expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", rounds=rounds, round_number=round_number, expected=expected):
                actual_result = list_contains_round(rounds, round_number)
                error_message = (
                    f"Called list_contains_round({rounds}, {round_number}). "
                    f"The function returned {actual_result}, but round {round_number} "
                    f"{'is' if expected else 'is not'} in {rounds}."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_card_average(self) -> None:
        """Test that card_average calculates the correct mean value of cards.

        Verifies that the function correctly computes the average value
        of all cards in the hand.
        """
        input_data = [[1], [5, 6, 7], [1, 2, 3, 4], [1, 10, 100]]
        result_data = [1.0, 6.0, 2.5, 37.0]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", hand=hand, expected=expected):
                actual_result = card_average(hand)
                error_message = (
                    f"Called card_average({hand}). "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} as the average of {hand}."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=5)
    def test_approx_average_is_average(self) -> None:
        """Test that approx_average_is_average compares approximation methods properly.

        Verifies that the function correctly determines if either the average of first and last cards
        or the middle card equals the true average of all cards in the hand.
        """
        input_data = [
            [0, 1, 5],
            [3, 6, 9, 12, 150],
            [1, 2, 3, 5, 9],
            [2, 3, 4, 7, 8],
            [1, 2, 3],
            [2, 3, 4],
            [2, 3, 4, 8, 8],
            [1, 2, 4, 5, 8],
        ]

        result_data = [False, False, False, False, True, True, True, True]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", hand=hand, expected=expected):
                actual_result = approx_average_is_average(hand)
                error_message = (
                    f"Called approx_average_is_average({hand}). "
                    f"The function returned {actual_result}, but "
                    f"the hand {hand} {'does' if expected else 'does not'} "
                    f"yield the same approximate average."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=6)
    def test_average_even_is_average_odd(self) -> None:
        """Test that average_even_is_average_odd compares even and odd indices correctly.

        Verifies that the function correctly determines if the average of cards at even indices
        equals the average of cards at odd indices.
        """
        input_data = [[5, 6, 8], [1, 2, 3, 4], [1, 2, 3], [5, 6, 7], [1, 3, 5, 7, 9]]
        result_data = [False, False, True, True, True]

        for variant, (input_hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", input_hand=input_hand, expected=expected):
                actual_result = average_even_is_average_odd(input_hand)
                error_message = (
                    f"Called average_even_is_average_odd({input_hand}). "
                    f"The function returned {actual_result}, but "
                    f"the hand {'does' if expected else 'does not'} "
                    f"yield the same odd-even average."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=7)
    def test_maybe_double_last(self) -> None:
        """Test that maybe_double_last doubles the last card if it's a Jack.

        Verifies that the function creates a copy of the hand and doubles the value
        of the last card only if it's a Jack (value 11).
        """
        input_data = [(1, 2, 11), (5, 9, 11), (5, 9, 10), (1, 2, 3), (1, 11, 8)]
        result_data = [[1, 2, 22], [5, 9, 22], [5, 9, 10], [1, 2, 3], [1, 11, 8]]

        for variant, (hand, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", hand=list(hand), expected=expected):
                actual_result = maybe_double_last(list(hand))
                error_message = (
                    f"Called maybe_double_last({list(hand)}). "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} as the maybe-doubled version of {list(hand)}."
                )

                assert actual_result == expected, error_message
