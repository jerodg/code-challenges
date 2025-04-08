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

Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number: The current round number.

    Returns:
        A list with the current round number and the following two round numbers.

    Example:
        >>> get_rounds(27)
        [27, 28, 29]
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1: The first list of rounds.
        rounds_2: The second list of rounds.

    Returns:
        A combined list with all rounds from rounds_1 followed by all rounds from rounds_2.

    Example:
        >>> concatenate_rounds([27, 28, 29], [35, 36])
        [27, 28, 29, 35, 36]
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check if the list of rounds contains the specified round number.

    Parameters:
        rounds: A list of round numbers.
        number: The round number to check for.

    Returns:
        True if the round number is in the list, False otherwise.

    Example:
        >>> list_contains_round([27, 28, 29, 35, 36], 29)
        True
        >>> list_contains_round([27, 28, 29, 35, 36], 30)
        False
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate the average value of cards in a hand.

    Parameters:
        hand: A list of card values.

    Returns:
        The average value of all cards in the hand.

    Example:
        >>> card_average([5, 6, 7])
        6.0
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Check if either of two approximation strategies yields the true average.

    Compares the true average with two approximation strategies:
    1. The average of the first and last card
    2. The value of the middle card (median for odd-length hands)

    Parameters:
        hand: A list of card values (odd-length).

    Returns:
        True if either approximation equals the true average, False otherwise.

    Example:
        >>> approx_average_is_average([1, 2, 3])
        True
        >>> approx_average_is_average([1, 2, 3, 5, 9])
        False
    """
    actual_avg = sum(hand) / len(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]  # Since all hands have odd length

    return actual_avg in {first_last_avg, median}


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Check if cards at even positions have the same average as cards at odd positions.

    Parameters:
        hand: A list of card values.

    Returns:
        True if the average of even-indexed cards equals the average of odd-indexed cards.

    Example:
        >>> average_even_is_average_odd([1, 2, 3])
        True
        >>> average_even_is_average_odd([1, 2, 3, 4])
        False
    """
    even_indexes = hand[0::2]  # Start at index 0, step by 2
    odd_indexes = hand[1::2]  # Start at index 1, step by 2

    even_avg = sum(even_indexes) / len(even_indexes)
    odd_avg = sum(odd_indexes) / len(odd_indexes)

    return even_avg == odd_avg


def maybe_double_last(hand: list[int]) -> list[int]:
    """Double the value of the last card if it's a Jack (11).

    Parameters:
        hand: A list of card values.

    Returns:
        A copy of the hand with the last card's value doubled if it's a Jack (11).

    Example:
        >>> maybe_double_last([5, 9, 11])
        [5, 9, 22]
        >>> maybe_double_last([5, 9, 10])
        [5, 9, 10]
    """
    result = hand.copy()  # Create a copy to avoid modifying the original
    if result and result[-1] == 11:  # Check if the last card is a Jack (11)
        result[-1] *= 2

    return result
