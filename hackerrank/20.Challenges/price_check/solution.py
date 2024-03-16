#!/usr/bin/env python3
"""

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""

def priceCheck(products, productPrices, productSold, soldPrice):
    errors = 0
    product_prices = {}

    # Create a dictionary of product prices
    for i in range(len(products)):
        product_prices[products[i]] = productPrices[i]

    # Check for pricing errors
    for i in range(len(productSold)):
        if product_prices[productSold[i]] != soldPrice[i]:
            errors += 1

    return errors
