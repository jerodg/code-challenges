"""Exercism Mecha Munch Management.

Functions to manage a user's shopping cart items.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def add_item(current_cart: dict, items_to_add: list | tuple) -> dict:
    """Add items to the shopping cart.

    Increases quantity for existing items or adds new items with a quantity of 1.
    """
    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1

    return current_cart


def read_notes(notes: list | tuple) -> dict:
    """Create a shopping cart from notes.

    Each item gets a quantity of 1.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict, recipe_updates: list[tuple[str, dict]]) -> dict:
    """Update recipe ideas.

    Updates existing recipes and adds new ones.
    """
    for recipe_name, recipe_update in recipe_updates:
        ideas[recipe_name] = recipe_update

    return ideas


def sort_entries(cart: dict) -> dict:
    """Sort shopping cart items alphabetically."""
    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Create a fulfillment cart for store ordering.

    Items are sorted in reverse alphabetical order with quantity, aisle, and
    refrigeration information.
    """
    fulfillment_cart = {}

    for item in cart:
        if item in aisle_mapping:
            fulfillment_cart[item] = [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]]

    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict) -> dict:
    """Update the store inventory based on a fulfillment cart.

    Reduces inventory by ordered quantities and marks items as 'Out of Stock'
    when depleted.
    """
    for item, details in fulfillment_cart.items():
        if item in store_inventory:
            ordered_quantity = details[0]
            current_quantity = store_inventory[item][0]

            if isinstance(current_quantity, int):
                new_quantity = current_quantity - ordered_quantity

                if new_quantity <= 0:
                    store_inventory[item][0] = "Out of Stock"
                else:
                    store_inventory[item][0] = new_quantity

    return store_inventory
