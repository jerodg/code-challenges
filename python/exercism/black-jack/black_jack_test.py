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
from black_jack import can_double_down, can_split_pairs, higher_card, is_blackjack, value_of_ace, value_of_card


class BlackJackTest(unittest.TestCase):
    """Test suite for the Black Jack card game implementation.

    This class contains test methods that verify the functionality of various
    card-related operations in a Black Jack game, including card value calculation,
    comparison of cards, determining optimal ace values, checking for blackjack hands,
    evaluating when pairs can be split, and when doubling down is allowed.
    """

    @pytest.mark.task(taskno=1)
    def test_value_of_card(self) -> None:
        """Test the value_of_card function with various card inputs.

        Verifies that the function correctly calculates the point value of
        different cards according to Black Jack rules (2-10 = face value,
        face cards = 10, Ace = 1).
        """
        test_data = [('2', 2), ('5', 5), ('8', 8), ('A', 1), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]

        for variant, (card, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', card=card, expected=expected):
                actual_result = value_of_card(card)
                error_msg = (
                    f'Called value_of_card({card}). '
                    f'The function returned {actual_result} as the value of the {card} card, '
                    f'but the test expected {expected} as the {card} card value.'
                )

                assert actual_result == expected, error_msg

    @pytest.mark.task(taskno=2)
    def test_higher_card(self) -> None:
        """Test the higher_card function with different card combinations.

        Verifies that the function correctly determines which of two cards has a higher value,
        or returns both cards as a tuple when they have equal value.
        """
        test_data = [
            ('A', 'A', ('A', 'A')),
            ('10', 'J', ('10', 'J')),
            ('3', 'A', '3'),
            ('3', '6', '6'),
            ('Q', '10', ('Q', '10')),
            ('4', '4', ('4', '4')),
            ('9', '10', '10'),
            ('6', '9', '9'),
            ('4', '8', '8'),
        ]

        for variant, (card_one, card_two, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', card_one=card_one, card_two=card_two, expected=expected):
                actual_result = higher_card(card_one, card_two)
                error_msg = (
                    f'Called higher_card({card_one}, {card_two}). '
                    f'The function returned {actual_result}, '
                    f'but the test expected {expected} as the result for the cards {card_one, card_two}.'
                )

                assert actual_result == expected, error_msg

    @pytest.mark.task(taskno=3)
    def test_value_of_ace(self) -> None:
        """Test the value_of_ace function with various hand compositions.

        Verifies that the function correctly determines the optimal value (1 or 11)
        for an ace card based on the existing cards in the hand to avoid exceeding 21.
        """
        test_data = [
            ('2', '3', 11),
            ('3', '6', 11),
            ('5', '2', 11),
            ('8', '2', 11),
            ('5', '5', 11),
            ('Q', 'A', 1),
            ('10', '2', 1),
            ('7', '8', 1),
            ('J', '9', 1),
            ('K', 'K', 1),
            ('2', 'A', 1),
            ('A', '2', 1),
        ]

        for variant, (card_one, card_two, ace_value) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', card_one=card_one, card_two=card_two, ace_value=ace_value):
                actual_result = value_of_ace(card_one, card_two)
                error_msg = (
                    f'Called value_of_ace({card_one}, {card_two}). '
                    f'The function returned {actual_result}, '
                    f'but the test expected {ace_value} as the value of an ace card '
                    f'when the hand includes {card_one, card_two}.'
                )

                assert value_of_ace(card_one, card_two) == ace_value, error_msg

    @pytest.mark.task(taskno=4)
    def test_is_blackjack(self) -> None:
        """Test the is_blackjack function with different card combinations.

        Verifies that the function correctly identifies hands that constitute a blackjack
        (an Ace and a 10-value card) and distinguishes them from other hands.
        """
        test_data = [
            (('A', 'K'), True),
            (('10', 'A'), True),
            (('10', '9'), False),
            (('A', 'A'), False),
            (('4', '7'), False),
            (('9', '2'), False),
            (('Q', 'K'), False),
        ]

        for variant, (hand, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', hand=hand, expected=expected):
                actual_result = is_blackjack(*hand)
                error_msg = (
                    f'Called is_blackjack({hand[0]}, {hand[1]}). '
                    f'The function returned {actual_result}, '
                    f'but hand {hand} {"is" if expected else "is not"} a blackjack.'
                )

                assert actual_result == expected, error_msg

    @pytest.mark.task(taskno=5)
    def test_can_split_pairs(self) -> None:
        """Test the can_split_pairs function with various card combinations.

        Verifies that the function correctly determines when a hand can be split
        into pairs (when both cards have the same value).
        """
        test_data = [(('Q', 'K'), True), (('6', '6'), True), (('A', 'A'), True), (('10', 'A'), False), (('10', '9'), False)]

        for variant, (hand, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', input=hand, expected=expected):
                actual_result = can_split_pairs(*hand)
                error_msg = (
                    f'Called can_split_pairs({hand[0]}, {hand[1]}). '
                    f'The function returned {actual_result}, '
                    f'but hand {hand} {"can" if expected else "cannot"} be split into pairs.'
                )

                assert actual_result == expected, error_msg

    @pytest.mark.task(taskno=6)
    def test_can_double_down(self) -> None:
        """Test the can_double_down function with different hands.

        Verifies that the function correctly determines when a player can double down
        (when the total value of the hand is 9, 10, or 11).
        """
        test_data = [
            (('A', '9'), True),
            (('K', 'A'), True),
            (('4', '5'), True),
            (('A', 'A'), False),
            (('10', '2'), False),
            (('10', '9'), False),
        ]

        for variant, (hand, expected) in enumerate(test_data, 1):
            with self.subTest(f'variation #{variant}', hand=hand, expected=expected):
                actual_result = can_double_down(*hand)
                error_msg = (
                    f'Called can_double_down({hand[0]}, {hand[1]}). '
                    f'The function returned {actual_result}, '
                    f'but hand {hand} {"can" if expected else "cannot"} be doubled down.'
                )

                assert actual_result == expected, error_msg
