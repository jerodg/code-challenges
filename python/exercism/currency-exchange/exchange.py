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

Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Convert currency using the provided exchange rate.

    Calculates the value of the budget in the target currency by dividing
    the budget by the exchange rate.

    Parameters:
        budget (float): The amount of money in the source currency to exchange.
        exchange_rate (float): The conversion rate from source to target currency.

    Returns:
        float: The amount of money in the target currency.

    Example:
        >>> exchange_money(100, 1.2)
        83.33333333333333
        >>> exchange_money(1000, 10)
        100.0
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate the money left after an exchange transaction.

    Computes the remaining amount from the budget after a certain value
    has been exchanged into another currency.

    Parameters:
        budget (float): The total amount of money available in the source currency.
        exchanging_value (float): The amount of the source currency being exchanged.

    Returns:
        float: The amount left in the source currency after the exchange.

    Example:
        >>> get_change(1000, 500)
        500.0
        >>> get_change(100, 75.5)
        24.5
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: float, number_of_bills: int) -> float:
    """Calculate the total value of bills of the same denomination.

    Determines the total monetary value by multiplying the denomination
    of each bill by the number of bills.

    Parameters:
        denomination (float): The value of a single bill.
        number_of_bills (int): The quantity of bills.

    Returns:
        float: The total value of all bills.

    Example:
        >>> get_value_of_bills(5, 10)
        50.0
        >>> get_value_of_bills(20, 4)
        80.0
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: float) -> int:
    """Calculate the maximum number of bills of a specific denomination from an amount.

    Determines how many whole bills of the given denomination can be obtained
    from the total amount using integer division.

    Parameters:
        amount (float): The total amount of money available.
        denomination (float): The value of a single bill.

    Returns:
        int: The maximum number of whole bills that can be obtained.

    Example:
        >>> get_number_of_bills(100, 20)
        5
        >>> get_number_of_bills(127.5, 5)
        25
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: float) -> float:
    """Calculate the remainder after dividing an amount into bills of a specific denomination.

    Determines the amount of money that cannot be distributed as whole bills
    of the given denomination using the modulo operator.

    Parameters:
        amount (float): The total amount of money available.
        denomination (float): The value of a single bill.

    Returns:
        float: The remaining amount that cannot be exchanged into whole bills.

    Example:
        >>> get_leftover_of_bills(100, 20)
        0.0
        >>> get_leftover_of_bills(126.5, 20)
        6.5
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: float, denomination: float) -> float:
    """Calculate the maximum exchangeable value in bills of a specific denomination.

    Determines the maximum amount that can be obtained in the target currency
    when accounting for exchange rate, spread percentage, and available bill denominations.

    Parameters:
        budget (float): The amount of money in the source currency to exchange.
        exchange_rate (float): The base conversion rate from source to target currency.
        spread (float): The percentage added to the exchange rate by the exchange service.
        denomination (float): The value of bills in the target currency.

    Returns:
        float: The maximum amount in the target currency that can be obtained in whole bills.

    Example:
        >>> exchangeable_value(100, 1.2, 10, 5)
        75.0
        >>> exchangeable_value(1500, 0.84, 25, 40)
        1000.0
    """
    actual_exchange_rate = exchange_rate * (1 + spread / 100)
    total_new_currency = budget / actual_exchange_rate
    max_bills = int(total_new_currency // denomination)
    return max_bills * denomination
