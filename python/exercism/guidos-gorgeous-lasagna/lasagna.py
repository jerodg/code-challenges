"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculates the remaining bake time for the lasagna based on a constant expected bake time.

    Args:
        elapsed_bake_time (int): The number of minutes the lasagna has been in the oven.

    Returns:
        int: The number of minutes remaining until the lasagna is done.

    Examples:
        >>> bake_time_remaining(30)
        10
        >>> bake_time_remaining(0)
        40
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """
    Calculates the preparation time based on the number of layers in the lasagna.

    Args:
        layers (int): The number of layers in the lasagna.

    Returns:
        int: Total preparation time in minutes.

    Examples:
        >>> preparation_time_in_minutes(1)
        2
        >>> preparation_time_in_minutes(4)
        8
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """
    Calculates the total elapsed cooking time for the lasagna.

    Args:
        layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has been baking.

    Returns:
        int: Total elapsed minutes spent on the lasagna, including preparation and baking time.

    Examples:
        >>> elapsed_time_in_minutes(3, 20)
        26
        >>> elapsed_time_in_minutes(1, 30)
        32
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
