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

import math
import unittest

import pytest
from exchange import exchange_money, exchangeable_value, get_change, get_leftover_of_bills, get_number_of_bills, get_value_of_bills


class CurrencyExchangeTest(unittest.TestCase):
    """Test suite for currency exchange functions.

    Tests various functions related to currency exchange operations including exchanging money,
    calculating change, determining bill values, and handling currency denominations.
    """

    @pytest.mark.task(taskno=1)
    def test_exchange_money(self) -> None:
        """Test the exchange_money function.

        Verifies that the exchange_money function correctly converts an amount from one
        currency to another using the given exchange rate.

        Test cases:
        - Converting 100000 with rate 0.8 should yield 125000
        - Converting 700000 with rate 10.0 should yield 70000
        """
        test_data = [(100000, 0.8), (700000, 10.0)]
        result_data = [125000, 70000]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchange_rate = params

            with self.subTest(f'variation #{variant}', budget=budget, exchange_rate=exchange_rate, expected=expected):
                actual_result = exchange_money(*params)
                error_message = (
                    f'Called exchange_money{budget, exchange_rate}. '
                    f'The function returned {actual_result}, but '
                    f'The tests expected {expected} when exchanging'
                    f' {budget} at a rate of {exchange_rate}.'
                )

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_get_change(self) -> None:
        """Test the get_change function.

        Verifies that the get_change function correctly calculates the amount
        left in the budget after exchanging a certain value.

        Test cases:
        - Budget 463000 with 5000 exchanged should leave 458000
        - Budget 1250 with 120 exchanged should leave 1130
        - Budget 15000 with 1380 exchanged should leave 13620
        """
        test_data = [(463000, 5000), (1250, 120), (15000, 1380)]
        result_data = [458000, 1130, 13620]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchanging_value = params

            with self.subTest(f'variation #{variant}', budget=budget, exchanging_value=exchanging_value, expected=expected):
                actual_result = get_change(*params)
                error_message = (
                    f'Called get_change{budget, exchanging_value}. '
                    f'The function returned {actual_result}, but '
                    f'The tests expected {expected} left in your budget.'
                )

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_get_value_of_bills(self) -> None:
        """Test the get_value_of_bills function.

        Verifies that the get_value_of_bills function correctly calculates the total
        value of bills by multiplying denomination by the number of bills.

        Test cases:
        - 128 bills of denomination 10000 should equal 1280000
        - 360 bills of denomination 50 should equal 18000
        - 200 bills of denomination 200 should equal 40000
        """
        test_data = [(10000, 128), (50, 360), (200, 200)]
        result_data = [1280000, 18000, 40000]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            denomination, number_of_bills = params

            with self.subTest(
                f'variation #{variant}', denomination=denomination, number_of_bills=number_of_bills, expected=expected
            ):
                actual_result = get_value_of_bills(*params)
                error_message = (
                    f'Called get_value_of_bills{denomination, number_of_bills}. '
                    f'The function returned {actual_result}, but '
                    f'The tests expected {expected} for the bills value.'
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_get_number_of_bills(self) -> None:
        """Test the get_number_of_bills function.

        Verifies that the get_number_of_bills function correctly calculates how many
        whole bills of a specific denomination can be obtained from an amount.

        Test cases:
        - Amount 163270 with denomination 50000 should yield 3 bills
        - Amount 54361 with denomination 1000 should yield 54 bills
        """
        test_data = [(163270, 50000), (54361, 1000)]
        result_data = [3, 54]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            amount, denomination = params

            with self.subTest(f'variation #{variant}', amount=amount, denomination=denomination, expected=expected):
                actual_result = get_number_of_bills(amount, denomination)
                error_message = (
                    f'Called get_number_of_bills{amount, denomination}. '
                    f'The function returned {actual_result} bills, but '
                    f'The tests expected {expected} bills.'
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=5)
    def test_get_leftover_of_bills(self) -> None:
        """Test the get_leftover_of_bills function.

        Verifies that the get_leftover_of_bills function correctly calculates the
        remainder after dividing an amount into bills of a specific denomination.

        Test cases:
        - Amount 10.1 with denomination 10 should have 0.1 leftover
        - Amount 654321.0 with denomination 5 should have 1.0 leftover
        - Amount pi with denomination 2 should have approximately 1.14 leftover
        """
        test_data = [(10.1, 10), (654321.0, 5), (math.pi, 2)]
        result_data = [0.1, 1.0, 1.14]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            amount, denomination = params

            with self.subTest(f'variation #{variant}', amount=amount, denomination=denomination, expected=expected):
                actual_result = get_leftover_of_bills(*params)
                error_message = (
                    f'Called get_leftover_of_bills{amount, denomination}. '
                    f'The function returned {actual_result}, but '
                    f'The tests expected {expected} as the leftover amount.'
                )

                self.assertAlmostEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=6)
    def test_exchangeable_value(self) -> None:
        """Test the exchangeable_value function.

        Verifies that the exchangeable_value function correctly calculates the maximum
        amount that can be obtained in the target currency when accounting for
        exchange rate, spread percentage, and available bill denominations.

        Test cases cover various scenarios with different budgets, exchange rates,
        spread percentages and denominations to ensure proper handling of edge cases.
        """
        test_data = [
            (100000, 10.61, 10, 1),
            (1500, 0.84, 25, 40),
            (470000, 1050, 30, 10000000000),
            (470000, 0.00000009, 30, 700),
            (425.33, 0.0009, 30, 700),
        ]

        result_data = [8568, 1400, 0, 4017094016600, 363300]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            budget, exchange_rate, spread, denomination = params

            with self.subTest(
                f'variation #{variant}',
                budget=budget,
                exchange_rate=exchange_rate,
                spread=spread,
                denomination=denomination,
                expected=expected,
            ):
                actual_result = exchangeable_value(budget, exchange_rate, spread, denomination)
                error_message = (
                    f'Called exchangeable_value{budget, exchange_rate, spread, denomination}. '
                    f'The function returned {actual_result}, but '
                    f'The tests expected {expected} as the maximum '
                    f'value of the new currency .'
                )

                assert actual_result == expected, error_message
