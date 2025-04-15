"""Exercism Test Inventory Management.

Test functions to keep track and alter inventory.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

import unittest

import pytest
from dicts import add_items, create_inventory, decrement_items, list_inventory, remove_item


class InventoryTest(unittest.TestCase):
    """Test suite for inventory management functions.

    This class contains unit tests that verify the functionality of various
    inventory management operations including creating inventories,
    adding/removing items, and listing inventory contents.
    """

    @pytest.mark.task(taskno=1)
    def test_create_inventory(self) -> None:
        """Test that create_inventory correctly counts occurrences of items in a list.

        Verifies that the function converts a list of items into a dictionary
        where keys are item names and values are the count of each item.
        """
        actual_result = create_inventory(["wood", "iron", "iron", "diamond", "diamond"])
        expected = {"wood": 1, "iron": 2, "diamond": 2}
        error_message = (
            'Called create_inventory(["wood", "iron", "iron", "diamond", "diamond"]). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_add_one_item(self) -> None:
        """Test adding multiple instances of a single item to inventory.

        Verifies that the function correctly increments the count for an existing item.
        """
        actual_result = add_items({"wood": 4, "iron": 2}, ["iron", "iron"])
        expected = {"wood": 4, "iron": 4}
        error_message = (
            'Called add_items({"wood": 4, "iron": 2}, ["iron", "iron"]). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_add_multiple_items(self) -> None:
        """Test adding multiple different items to inventory.

        Verifies that the function correctly increments counts for multiple item types.
        """
        actual_result = add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"])
        expected = {"wood": 3, "gold": 3, "diamond": 3}
        error_message = (
            'Called add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"]). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_add_new_item(self) -> None:
        """Test adding new items that don't exist in the inventory yet.

        Verifies that the function adds new items to the inventory with correct counts.
        """
        actual_result = add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"])
        expected = {"iron": 2, "diamond": 2, "wood": 2}
        error_message = (
            'Called add_items({"iron": 1, "diamond": 2}, ["iron", "wood", "wood"]). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_add_from_empty_dict(self) -> None:
        """Test adding items to an empty inventory.

        Verifies that the function works correctly when starting with an empty dictionary.
        """
        actual_result = add_items({}, ["iron", "iron", "diamond"])
        expected = {"iron": 2, "diamond": 1}
        error_message = (
            'Called add_items({}, ["iron", "iron", "diamond"]). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_decrement_items(self) -> None:
        """Test decrementing items from inventory.

        Verifies that the function correctly decreases counts for existing items.
        """
        actual_result = decrement_items({"iron": 3, "diamond": 4, "gold": 2}, ["iron", "iron", "diamond", "gold", "gold"])
        expected = {"iron": 1, "diamond": 3, "gold": 0}
        error_message = (
            'Called decrement_items({"iron": 3, "diamond": 4, "gold": 2},'
            '["iron", "iron", "diamond", "gold", "gold"]). The function '
            f"returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_not_below_zero(self) -> None:
        """Test that item counts don't go below zero when decrementing.

        Verifies that the function ensures item counts never become negative.
        """
        actual_result = decrement_items(
            {"wood": 2, "iron": 3, "diamond": 1}, ["wood", "wood", "wood", "iron", "diamond", "diamond"]
        )
        expected = {"wood": 0, "iron": 2, "diamond": 0}
        error_message = (
            'Called decrement_items({"wood": 2, "iron": 3, "diamond": 1}, '
            '["wood", "wood", "wood", "iron", "diamond", "diamond"]). The '
            f"function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_decrement_items_not_in_inventory(self) -> None:
        """Test decrementing items that don't exist in inventory.

        Verifies that the function safely handles attempts to decrement non-existent items.
        """
        actual_result = decrement_items({"iron": 3, "gold": 2}, ["iron", "wood", "iron", "diamond"])

        expected = {"iron": 1, "gold": 2}
        error_message = (
            'Called decrement_items({"iron": 3, "gold": 2}, '
            '["iron", "wood", "iron", "diamond"]). The function '
            f"returned {actual_result}, but the tests "
            f"expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_remove_item(self) -> None:
        """Test completely removing an item from inventory.

        Verifies that the function removes an item key from the dictionary.
        """
        actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond")
        expected = {"iron": 1, "gold": 1}
        error_message = (
            'Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"). '
            f"The function returned {actual_result}, but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_remove_item_not_in_inventory(self) -> None:
        """Test removing an item that's not in the inventory.

        Verifies that the function handles attempts to remove non-existent items without error.
        """
        actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")
        expected = {"iron": 1, "gold": 1, "diamond": 2}
        error_message = (
            'Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood"). '
            f"The function returned {actual_result}, "
            f"but the tests expected {expected}."
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=5)
    def test_list_inventory(self) -> None:
        """Test listing inventory items with counts greater than zero.

        Verifies that the function returns a list of tuples containing only items
        with positive counts, excluding those with zero counts.
        """
        actual_result = list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0})
        expected = [("coal", 15), ("diamond", 3), ("wood", 67)]
        error_message = (
            'Called list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}). '
            f"The function returned {actual_result}, "
            f"but the tests expected {expected}."
        )

        assert actual_result == expected, error_message
