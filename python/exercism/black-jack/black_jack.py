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

Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card in Blackjack.

    In Blackjack, face cards (J, Q, K) are worth 10 points,
    Ace (A) is worth 1 point (or 11 in some contexts, handled elsewhere),
    and number cards are worth their face value.

    Parameters:
        card (str): A string representing a playing card ('2' through '10', 'J', 'Q', 'K', 'A').

    Returns:
        int: The point value of the card according to Blackjack rules.

    Example:
        >>> value_of_card('K')
        10
        >>> value_of_card('A')
        1
        >>> value_of_card('7')
        7
    """
    # Face cards are worth 10 points
    if card in {'J', 'Q', 'K'}:
        return 10

    # Ace is worth 1 point in this context
    if card == 'A':
        return 1

    # Number cards are worth their face value
    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in a Blackjack hand.

    Compares two cards and returns the one with the higher value.
    If both cards have the same value, returns both cards as a tuple.

    Parameters:
        card_one (str): A string representing the first playing card.
        card_two (str): A string representing the second playing card.

    Returns:
        str | tuple[str, str]: The higher-valued card, or a tuple of both cards
                               if they have equal value.

    Example:
        >>> higher_card('K', '3')
        'K'
        >>> higher_card('Q', 'K')
        ('Q', 'K')
        >>> higher_card('6', 'A')
        '6'
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one

    if value_two > value_one:
        return card_two

    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an ace card in Blackjack.

    In Blackjack, an ace can be worth either 1 or 11 points. This function determines
    the optimal value for an additional ace based on the total value of the existing hand.
    If using 11 would cause the hand to exceed 21 points, the ace is valued at 1.

    Parameters:
        card_one (str): A string representing the first card in the hand.
        card_two (str): A string representing the second card in the hand.

    Returns:
        int: The optimal value of a new ace card (either 1 or 11) based on the current hand.

    Example:
        >>> value_of_ace('K', '5')
        1
        >>> value_of_ace('2', '3')
        11
        >>> value_of_ace('A', 'A')
        1
    """
    # Calculate the sum of the existing cards
    total = 0

    if card_one in {'J', 'Q', 'K', '10'}:
        total += 10
    elif card_one == 'A':
        total += 11
    else:
        total += int(card_one)

    if card_two in {'J', 'Q', 'K', '10'}:
        total += 10
    elif card_two == 'A':
        total += 11
    else:
        total += int(card_two)

    # Decide if the new ace should be 1 or 11
    if total + 11 <= 21:
        return 11

    return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    In Blackjack, a natural or blackjack is a hand consisting of an Ace
    and a 10-value card (10, Jack, Queen, or King) as the first two cards.

    Parameters:
        card_one (str): A string representing the first card in the hand.
        card_two (str): A string representing the second card in the hand.

    Returns:
        bool: True if the hand is a blackjack, False otherwise.

    Example:
        >>> is_blackjack('A', 'K')
        True
        >>> is_blackjack('10', 'A')
        True
        >>> is_blackjack('10', 'J')
        False
    """
    is_ace = card_one == 'A' or card_two == 'A'
    is_ten_card = (card_one in {'10', 'J', 'Q', 'K'}) or (card_two in {'10', 'J', 'Q', 'K'})

    return is_ace and is_ten_card


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    In Blackjack, a player can split their hand when they have two cards of the same value.
    This creates two separate hands that are played independently.

    Parameters:
        card_one (str): A string representing the first card in the hand.
        card_two (str): A string representing the second card in the hand.

    Returns:
        bool: True if the cards can be split (have equal value), False otherwise.

    Example:
        >>> can_split_pairs('Q', 'K')
        True
        >>> can_split_pairs('10', 'J')
        True
        >>> can_split_pairs('A', '10')
        False
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    In Blackjack, players can double down (double their initial bet)
    when their first two cards total 9, 10, or 11 points.

    Parameters:
        card_one (str): A string representing the first card in the hand.
        card_two (str): A string representing the second card in the hand.

    Returns:
        bool: True if the player can double down (hand totals 9, 10, or 11), False otherwise.

    Example:
        >>> can_double_down('5', '4')
        True
        >>> can_double_down('A', '9')
        True
        >>> can_double_down('K', 'Q')
        False
    """
    total = value_of_card(card_one) + value_of_card(card_two)

    return total in {9, 10, 11}
