"""Exercism Inventory Management.

Functions to keep track and alter inventory.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def create_inventory(items: list) -> dict:
    """Create a dictionary that tracks the count of each item in a list.

    The function iterates through the input list and builds a frequency counter,
    incrementing the count for each occurrence of an item.

    Parameters:
        items: List of items to create an inventory from.

    Returns:
        A dictionary with items as keys and their counts as values.

    Example:
        >>> create_inventory(["coal", "wood", "wood", "diamond"])
        {"coal": 1, "wood": 2, "diamond": 1}
    """
    inventory = {}
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items list.

    This function updates the inventory dictionary by incrementing the count for each item
    in the input list. If an item doesn't exist in the inventory yet, it adds it with a count of 1.

    Parameters:
        inventory: Dictionary of existing inventory.
        items: List of items to update the inventory with.

    Returns:
        The inventory updated with the new items.

    Example:
        >>> inventory = {"coal": 1, "diamond": 1}
        >>> add_items(inventory, ["coal", "wood", "wood"])
        {"coal": 2, "diamond": 1, "wood": 2}
    """
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the items list.

    This function reduces the count for each item in the input list that exists in the inventory.
    It ensures item counts never go below zero by only decrementing when the count is positive.

    Parameters:
        inventory: Dictionary of existing inventory.
        items: List of items to decrement from the inventory.

    Returns:
        The inventory updated with items decremented.

    Example:
        >>> inventory = {"coal": 3, "diamond": 1, "wood": 2}
        >>> decrement_items(inventory, ["coal", "coal", "diamond", "wood", "not_found"])
        {"coal": 1, "diamond": 0, "wood": 1}
    """
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches the item string.

    This function completely removes an item entry from the inventory dictionary
    if the item exists as a key, regardless of its count.

    Parameters:
        inventory: Dictionary of existing inventory.
        item: Item to remove from the inventory.

    Returns:
        The inventory with the specified item removed, or unchanged if the item wasn't found.

    Example:
        >>> inventory = {"coal": 2, "diamond": 1, "wood": 3}
        >>> remove_item(inventory, "coal")
        {"diamond": 1, "wood": 3}
    """
    if item in inventory:
        inventory.pop(item)

    return inventory


def list_inventory(inventory: dict) -> list[tuple[str, int]]:
    """Create a list of items in inventory that have a count greater than zero.

    This function filters the inventory to include only items with positive counts,
    converting the filtered inventory dictionary into a list of (item, count) tuples.

    Parameters:
        inventory: Dictionary of existing inventory.

    Returns:
        A list of tuples containing item name and count for all items with count > 0.

    Example:
        >>> inventory = {"coal": 2, "diamond": 0, "wood": 3}
        >>> list_inventory(inventory)
        [("coal", 2), ("wood", 3)]
    """
    return [(item, count) for item, count in inventory.items() if count > 0]
