"""Exercism Test Mecha Munch Management.

Test functions to manage a user's shopping cart items.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
import unittest
from collections import OrderedDict

import pytest
from dict_methods import (
    add_item,
    read_notes,
    send_to_store,
    sort_entries,
    update_recipes,
    update_store_inventory,
)
from dict_methods_test_data import (
    add_item_data,
    read_notes_data,
    send_to_store_data,
    sort_entries_data,
    update_recipes_data,
    update_store_inventory_data,
)


class MechaMunchManagementTest(unittest.TestCase):
    """Unit tests for Mecha Munch Management functions.

    This class contains test cases for various functions that manage a user's
    shopping cart, recipes, and store inventory. Each test method corresponds
    to a specific function in the `dict_methods` module.
    """

    @pytest.mark.task(taskno=1)
    def test_add_item(self):
        """Test the `add_item` function.

        Iterates through test cases to verify that items are correctly added
        to the shopping cart. Ensures that quantities are updated for existing
        items and new items are added with a quantity of 1.
        """
        for variant, (input_data, expected) in enumerate(add_item_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = add_item(input_data[0], input_data[1])
                error_msg = (f'Called add_item({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the item was added.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_read_notes(self):
        """Test the `read_notes` function.

        Iterates through test cases to verify that a shopping cart is correctly
        created from a list of notes. Ensures that all items are added with a
        default quantity of 1.
        """
        for variant, (input_data, expected) in enumerate(read_notes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = read_notes(input_data)
                error_msg = (f'Called read_notes({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the notes were read.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_update_recipes(self):
        """Test the `update_recipes` function.

        Iterates through test cases to verify that recipe ideas are correctly
        updated. Ensures that existing recipes are modified and new recipes
        are added as needed.
        """
        for variant, (input_data, expected) in enumerate(update_recipes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_recipes(input_data[0], input_data[1])
                error_msg = (f"Called update_recipes({input_data[0]}, {input_data[1]}). "
                             f"The function returned {actual_result}, but the tests "
                             f"expected: {expected} once the recipes were updated.")

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_sort_entries(self):
        """Test the `sort_entries` function.

        Iterates through test cases to verify that the shopping cart is sorted
        alphabetically by item name. Ensures that the returned dictionary is
        correctly ordered.
        """
        for variant, (input_data, expected) in enumerate(sort_entries_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expecred=expected):
                actual_result = sort_entries(input_data)
                error_msg = (f'Called sort_entries({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} for the sorted entries.')

                # Convert to OrderedDict to ensure order is considered during comparison.
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_send_to_store(self):
        """Test the `send_to_store` function.

        Iterates through test cases to verify that the fulfillment cart is
        correctly created. Ensures that quantities, aisle information, and
        refrigeration requirements are combined and sorted in reverse
        alphabetical order.
        """
        for variant, (input_data, expected) in enumerate(send_to_store_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = send_to_store(input_data[0], input_data[1])
                error_msg = (f'Called send_to_store({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the fulfillment cart.')

                # Convert to OrderedDict to ensure order is considered during comparison.
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=6)
    def test_update_store_inventory(self):
        """Test the `update_store_inventory` function.

        Iterates through test cases to verify that the store inventory is
        correctly updated based on the fulfillment cart. Ensures that item
        quantities are reduced and items are marked as 'Out of Stock' when
        depleted.
        """
        for variant, (input_data, expected) in enumerate(update_store_inventory_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_store_inventory(input_data[0], input_data[1])
                error_msg = (f'Called update_store_inventory({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the store inventory.')

                self.assertEqual(actual_result, expected, msg=error_msg)
