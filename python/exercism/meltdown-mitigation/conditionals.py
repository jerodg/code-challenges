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

Functions to prevent a nuclear meltdown.
"""


def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Determine if the reactor criticality is balanced.

    This function checks whether the nuclear reactor is in a balanced state
    based on temperature, neutron emission rate, and their combined effect.
    A reactor is considered balanced when all three conditions are met.

    Parameters:
        temperature (float): The temperature of the reactor core in kelvin.
        neutrons_emitted (float): The number of neutrons being emitted per second.

    Returns:
        bool: True if the reactor is in a balanced state, False otherwise.

    Example:
        >>> is_criticality_balanced(750, 650)
        True
        >>> is_criticality_balanced(800, 500)
        False
    """
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage: float, current: float, theoretical_max_power: float) -> str:
    """Evaluate the reactor efficiency zone based on power output.

    This function calculates the actual power output as a percentage of the
    theoretical maximum power and returns a color-coded efficiency band.

    Parameters:
        voltage (float): The voltage value produced by the reactor.
        current (float): The current value produced by the reactor in amperes.
        theoretical_max_power (float): The theoretical maximum power output.

    Returns:
        str: A color indicating the efficiency range:
            - 'green' for efficiency >= 80%
            - 'orange' for 60% <= efficiency < 80%
            - 'red' for 30% <= efficiency < 60%
            - 'black' for efficiency < 30%

    Example:
        >>> reactor_efficiency(200, 50, 15000)
        'orange'
        >>> reactor_efficiency(10, 99, 1000)
        'green'
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str:
    """Assess the reactor's status based on the output of the core.

    This function calculates the product of temperature and neutrons produced per second,
    comparing it with a threshold to determine the reactor's operational status.

    Parameters:
        temperature (float): The temperature value of the reactor core.
        neutrons_produced_per_second (float): The number of neutrons produced per second.
        threshold (float): The threshold value for determining the reactor's status.

    Returns:
        str: A status indicator:
            - 'LOW' when product < 90% of threshold
            - 'NORMAL' when product is between 90% and 110% of threshold (inclusive)
            - 'DANGER' when product > 110% of threshold

    Example:
        >>> fail_safe(200, 50, 15000)
        'LOW'
        >>> fail_safe(800, 600, 500000)
        'NORMAL'
        >>> fail_safe(800, 700, 500000)
        'DANGER'
    """
    product = temperature * neutrons_produced_per_second

    if product < 0.9 * threshold:
        return 'LOW'

    if product <= 1.1 * threshold:
        return 'NORMAL'

    return 'DANGER'
