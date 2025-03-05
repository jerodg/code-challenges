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

Unit tests for the Pac-Man arcade game logic.

This module contains unit tests for the core gameplay functions of a Pac-Man-like arcade game.
It uses the unittest framework and pytest for marking specific tasks.
Each test verifies the correctness of the game logic functions such as eating ghosts, scoring points,
losing the game, and winning the game.
"""

import unittest

import pytest
from arcade_game import eat_ghost, lose, score, win


class GhostGobbleGameTest(unittest.TestCase):
    """Unit tests for the Pac-Man arcade game logic functions.

    This class contains unit tests for the core gameplay functions of a Pac-Man-like arcade game.
    It uses the unittest framework and pytest for marking specific tasks. Each test verifies the
    correctness of the game logic functions such as eating ghosts, scoring points, losing the game,
    and winning the game.
    """


@pytest.mark.task(taskno=1)
def test_ghost_gets_eaten(self) -> None:
    """Verify that ghosts can be eaten when conditions are met.

    Tests the eat_ghost function with a power pellet active and player touching
    a ghost, which should result in the ghost being eaten (True).
    """
    actual_result = eat_ghost(True, True)
    # Construct a detailed error message to provide clear context if the test fails
    error_message = (
        'Called eat_ghost(True, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the ghost gets eaten (True).'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=1)
def test_ghost_does_not_get_eaten_because_no_power_pellet_active(self) -> None:
    """Verify the ghost remains uneaten when power pellet is not active.

    Tests the eat_ghost function with no power pellet active but player touching
    a ghost, which should result in the ghost not being eaten (False).
    """
    actual_result = eat_ghost(False, True)
    # Construct a detailed error message to provide clear context if the test fails
    error_message = (
        'Called eat_ghost(False, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'ghost **does not** get eaten because '
        'no power pellet was active.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=1)
def test_ghost_does_not_get_eaten_because_not_touching_ghost(self) -> None:
    """Verify that ghosts cannot be eaten when the player isn't touching them.

    Tests the eat_ghost function with an active power pellet but the player not
    touching a ghost, which should result in the ghost not being eaten (False).
    """
    actual_result = eat_ghost(True, False)
    error_message = (
        'Called eat_ghost(True, False).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'ghost **does not** get eaten because '
        'the player was not touching the ghost.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=2)
def test_score_when_eating_dot(self) -> None:
    """Verify that the player scores points when touching a dot.

    Tests the score function when the player is touching a dot but not a power pellet,
    which should result in the player scoring points (True).
    """
    actual_result = score(False, True)
    error_message = (
        'Called score(False, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player scores because they were touching a dot.'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=2)
def test_score_when_eating_power_pellet(self) -> None:
    """Verify that the player scores points when touching a power pellet.

    Tests the score function when the player is touching a power pellet but not a dot,
    which should result in the player scoring points (True).
    """
    actual_result = score(True, False)
    error_message = (
        'Called score(True, False).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player scores because they '
        'were touching a power pellet.'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=2)
def test_no_score_when_nothing_eaten(self) -> None:
    """Verify that the player doesn't score points when touching neither dot nor power pellet.

    Tests the score function when the player is not touching a dot or a power pellet,
    which should result in the player not scoring any points (False).
    """
    actual_result = score(False, False)
    error_message = (
        'Called score(False, False).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player **does not** score because they '
        'were not touching anything.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=3)
def test_lose_if_touching_a_ghost_without_a_power_pellet_active(self) -> None:
    """Verify that the player loses when touching a ghost without an active power pellet.

    Tests the lose function when the player touches a ghost without having a power pellet active,
    which should result in the player losing the game (True).
    """
    actual_result = lose(False, True)
    error_message = (
        'Called lose(False, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player loses because they touched a '
        'ghost without a power pellet activated.'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=3)
def test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active(self) -> None:
    """Verify that the player doesn't lose when touching a ghost with an active power pellet.

    Tests the lose function when the player touches a ghost while having a power pellet active,
    which should result in the player not losing the game (False).
    """
    actual_result = lose(True, True)
    error_message = (
        'Called lose(True, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player **does not** lose because when they touched a '
        'ghost, a power pellet was active.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=3)
def test_dont_lose_if_not_touching_a_ghost(self) -> None:
    """Verify that the player doesn't lose when not touching a ghost.

    Tests the lose function when the player is not touching a ghost (regardless of power pellet status),
    which should result in the player not losing the game (False).
    """
    actual_result = lose(True, False)
    error_message = (
        'Called lose(True, False).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player **does not** lose because they were '
        'not touching a ghost.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=4)
def test_win_if_all_dots_eaten(self) -> None:
    """Verify that the player wins when all dots are eaten and not touching a ghost.

    Tests the win function when the player has eaten all dots and is not touching a ghost,
    which should result in the player winning the game (True).
    """
    actual_result = win(True, False, False)
    error_message = (
        'Called win(True, False, False).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player wins because all the dots were eaten.'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=4)
def test_dont_win_if_all_dots_eaten_but_touching_a_ghost(self) -> None:
    """Verify that the player doesn't win when touching a ghost without a power pellet.

    Tests the win function when the player has eaten all dots but is touching a ghost without
    an active power pellet, which should result in the player not winning the game (False).
    """
    actual_result = win(True, False, True)
    error_message = (
        'Called win(True, False, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the '
        'player **does not** win, because '
        'the player was touching a ghost.'
    )
    assert actual_result is False, error_message


@pytest.mark.task(taskno=4)
def test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active(self) -> None:
    """Verify that the player wins when all dots are eaten and touching a ghost with a power pellet.

    Tests the win function when the player has eaten all dots and is touching a ghost with an
    active power pellet, which should result in the player winning the game (True).
    """
    actual_result = win(True, True, True)
    error_message = (
        'Called win(True, True, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the player wins, '
        f'because a power pellet was active when they '
        f'touched a ghost.'
    )
    assert actual_result is True, error_message


@pytest.mark.task(taskno=4)
def test_dont_win_if_not_all_dots_eaten(self) -> None:
    """Verify that the player doesn't win when not all dots are eaten.

    Tests the win function when the player has not eaten all dots (regardless of power pellet
    status or ghost contact), which should result in the player not winning the game (False).
    """
    actual_result = win(False, True, True)
    error_message = (
        'Called win(False, True, True).'
        f'The function returned {actual_result}, but the '
        f'tests expected that the player **does not** win, '
        f'because the player did not eat all of the dots.'
    )
    assert actual_result is False, error_message
