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

Functions for the Pac-Man arcade game logic.

This module provides the core gameplay functions for a Pac-Man-like arcade game,
handling the interactions between the player, ghosts, dots and power pellets.
Each function implements a specific game rule to determine outcomes like scoring,
winning, losing, and ghost interactions.
"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify if the player can eat a ghost.

    The player can only eat a ghost if a power pellet is active
    and they are touching a ghost.

    Parameters:
        power_pellet_active (bool): Whether the player has an active power pellet.
        touching_ghost (bool): Whether the player is touching a ghost.

    Returns:
        bool: True if the player can eat the ghost, False otherwise.

    Example:
        >>> eat_ghost(True, True)
        True
        >>> eat_ghost(False, True)
        False
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verify if the player scores points.

    The player scores points when they either touch a power pellet or a dot.

    Parameters:
        touching_power_pellet (bool): Whether the player is touching a power pellet.
        touching_dot (bool): Whether the player is touching a dot.

    Returns:
        bool: True if the player scores points, False otherwise.

    Example:
        >>> score(True, False)
        True
        >>> score(False, True)
        True
        >>> score(False, False)
        False
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify if the player loses the game.

    The player loses when they touch a ghost without an active power pellet.

    Parameters:
        power_pellet_active (bool): Whether the player has an active power pellet.
        touching_ghost (bool): Whether the player is touching a ghost.

    Returns:
        bool: True if the player loses the game, False otherwise.

    Example:
        >>> lose(False, True)
        True
        >>> lose(True, True)
        False
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify if the player wins the game.

    The player wins when they've eaten all dots and either:
    - They're not touching a ghost, or
    - They're touching a ghost but have an active power pellet

    Parameters:
        has_eaten_all_dots (bool): Whether the player has eaten all dots.
        power_pellet_active (bool): Whether the player has an active power pellet.
        touching_ghost (bool): Whether the player is touching a ghost.

    Returns:
        bool: True if the player wins the game, False otherwise.

    Example:
        >>> win(True, False, False)
        True
        >>> win(True, False, True)
        False
        >>> win(False, True, False)
        False
    """
    return has_eaten_all_dots and (not touching_ghost or power_pellet_active)
