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
from conditionals import fail_safe, is_criticality_balanced, reactor_efficiency


class MeltdownMitigationTest(unittest.TestCase):
    """Test cases for Meltdown mitigation exercise.

    This class contains test methods for the three main functions of the
    meltdown mitigation system: criticality balance check, reactor efficiency
    evaluation, and fail-safe mechanism.
    """

    @pytest.mark.task(taskno=1)
    def test_is_criticality_balanced(self) -> None:
        """Test the criticality balance function with various edge cases.

        This test verifies that the is_criticality_balanced function correctly
        determines if a reactor is in a balanced state based on temperature and
        neutron emission values at various boundary conditions.

        Testing border cases around typical points:
        T, n == (800, 500), (625, 800), (500, 1000), etc.
        """
        test_data = (
            (750, 650, True),
            (799, 501, True),
            (500, 600, True),
            (1000, 800, False),
            (800, 500, False),
            (800, 500.01, False),
            (799.99, 500, False),
            (500.01, 999.99, False),
            (625, 800, False),
            (625.99, 800, False),
            (625.01, 799.99, False),
            (799.99, 500.01, True),
            (624.99, 799.99, True),
            (500, 1000, False),
            (500.01, 1000, False),
            (499.99, 1000, True),
        )

        for variant, data in enumerate(test_data, start=1):
            temp, neutrons_emitted, expected = data
            with self.subTest(f'variation #{variant}', temp=temp, neutrons_emitted=neutrons_emitted, expected=expected):
                # pylint: disable=assignment-from-no-return
                actual_result = is_criticality_balanced(temp, neutrons_emitted)
                failure_message = (
                    f'Called is_criticality_balanced({temp}, {neutrons_emitted}). '
                    f' The function returned {actual_result}, '
                    f'but the test expected {expected} as the return value.'
                )

                assert actual_result == expected, failure_message

    @pytest.mark.task(taskno=2)
    def test_reactor_efficiency(self) -> None:
        """Test the reactor efficiency function across different efficiency bands.

        This test verifies that the reactor_efficiency function correctly
        categorizes power output into efficiency bands (green, orange, red, black)
        based on the percentage of theoretical maximum power.
        """
        voltage = 10
        theoretical_max_power = 10000

        # The numbers are chosen so that current == 10 x percentage
        test_data = (
            (1000, 'green'),  # 100% efficiency
            (999, 'green'),  # 99.9% efficiency
            (800, 'green'),  # 80% efficiency
            (799, 'orange'),  # 79.9% efficiency
            (700, 'orange'),  # 70% efficiency
            (600, 'orange'),  # 60% efficiency
            (599, 'red'),  # 59.9% efficiency
            (560, 'red'),  # 56% efficiency
            (400, 'red'),  # 40% efficiency
            (300, 'red'),  # 30% efficiency
            (299, 'black'),  # 29.9% efficiency
            (200, 'black'),  # 20% efficiency
            (0, 'black'),  # 0% efficiency
        )

        for variant, data in enumerate(test_data, start=1):
            current, expected = data
            with self.subTest(
                f'variation #{variant}',
                voltage=voltage,
                current=current,
                theoretical_max_power=theoretical_max_power,
                expected=expected,
            ):
                # pylint: disable=assignment-from-no-return
                actual_result = reactor_efficiency(voltage, current, theoretical_max_power)
                failure_message = (
                    f'Called reactor_efficiency({voltage}, {current}, {theoretical_max_power}). '
                    f'The function returned {actual_result}, '
                    f'but the test expected {expected} as the return value.'
                )

                assert actual_result == expected, failure_message

    @pytest.mark.task(taskno=3)
    def test_fail_safe(self) -> None:
        """Test the fail-safe mechanism across different operational statuses.

        This test verifies that the fail_safe function correctly determines
        the reactor's status (LOW, NORMAL, DANGER) based on the relationship
        between the product of temperature and neutrons per second compared to
        a threshold value.
        """
        temp = 10
        threshold = 10000
        test_data = (
            (399, 'LOW'),  # 39.9% of threshold
            (300, 'LOW'),  # 30% of threshold
            (1, 'LOW'),  # 0.1% of threshold
            (0, 'LOW'),  # 0% of threshold
            (901, 'NORMAL'),  # 90.1% of threshold
            (1000, 'NORMAL'),  # 100% of threshold
            (1099, 'NORMAL'),  # 109.9% of threshold
            (899, 'LOW'),  # 89.9% of threshold
            (700, 'LOW'),  # 70% of threshold
            (400, 'LOW'),  # 40% of threshold
            (1101, 'DANGER'),  # 110.1% of threshold
            (1200, 'DANGER'),  # 120% of threshold
        )

        for variant, (neutrons_per_second, expected) in enumerate(test_data, start=1):
            with self.subTest(
                f'variation #{variant}', temp=temp, neutrons_per_second=neutrons_per_second, threshold=threshold, expected=expected
            ):
                # pylint: disable=assignment-from-no-return
                actual_result = fail_safe(temp, neutrons_per_second, threshold)
                failure_message = (
                    f'Called fail_safe({temp}, {neutrons_per_second}, {threshold}). '
                    f'The function returned {actual_result}, '
                    f'but the test expected {expected} as the return value.'
                )

                assert actual_result == expected, failure_message
