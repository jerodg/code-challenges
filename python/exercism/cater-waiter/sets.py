"""Exercism Cater Waiter.

Functions for compiling dishes and ingredients for a catering company.
This module implements various set operations to manage recipe data.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
from sets_categories_data import ALCOHOLS, KETO, PALEO, SPECIAL_INGREDIENTS, VEGAN, VEGETARIAN


def clean_ingredients(dish_name: str, dish_ingredients: list[str]) -> tuple[str, set[str]]:
    """Convert dish ingredients to a set and pair with the dish name.

    Removes duplicate ingredients by converting the list to a set.

    Parameters:
        dish_name: The name of the dish.
        dish_ingredients: List of ingredients for the dish.

    Returns:
        A tuple containing the dish name and a set of unique ingredients.

    Example:
        >>> clean_ingredients("Pasta", ["Tomato", "Basil", "Tomato"])
        ('Pasta', {'Tomato', 'Basil'})
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    """Determine if a drink is a cocktail or mocktail.

    Uses set intersection to check if any ingredients are alcoholic.
    
    Parameters:
        drink_name: The name of the drink.
        drink_ingredients: List of ingredients in the drink.

    Returns:
        A string indicating whether the drink is a cocktail or mocktail.

    Example:
        >>> check_drinks("Mojito", ["Rum", "Mint", "Lime"])
        'Mojito Cocktail'
    """
    if ALCOHOLS & set(drink_ingredients):
        return f"{drink_name} Cocktail"

    return f"{drink_name} Mocktail"


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    """Classify a dish into dietary categories based on its ingredients.

    Uses set subset operations to test if ingredients fit into dietary categories.
    Categories are checked in order of restrictiveness.

    Parameters:
        dish_name: The name of the dish.
        dish_ingredients: List of ingredients in the dish.

    Returns:
        A string showing the dish name and its dietary category.

    Example:
        >>> categorize_dish("Tofu Stir-Fry", ["Tofu", "Vegetables", "Soy Sauce"])
        'Tofu Stir-Fry: VEGAN'
    """
    ingredient_set = set(dish_ingredients)

    if ingredient_set.issubset(VEGAN):
        return f"{dish_name}: VEGAN"

    if ingredient_set.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"

    if ingredient_set.issubset(PALEO):
        return f"{dish_name}: PALEO"

    if ingredient_set.issubset(KETO):
        return f"{dish_name}: KETO"

    return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish: tuple[str, list[str]]) -> tuple[str, set[str]]:
    """Identify special ingredients in a dish.

    Uses set intersection to find ingredients that are in the special ingredients list.

    Parameters:
        dish: A tuple containing the dish name and a list of ingredients.

    Returns:
        A tuple with the dish name and a set of its special ingredients.

    Example:
        >>> tag_special_ingredients(("Pasta", ["Tomato", "Garlic", "Olives"]))
        ('Pasta', {'Garlic'})
    """
    dish_name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS

    return (dish_name, special)


def compile_ingredients(recipe_sets: list[set[str]]) -> set[str]:
    """Combine all ingredients from multiple recipe sets.

    Uses set union to create a comprehensive set of all ingredients.

    Parameters:
        recipe_sets: A list of sets, where each set contains ingredients for a recipe.

    Returns:
        A set containing all unique ingredients from all recipes.

    Example:
        >>> compile_ingredients([{'Garlic', 'Salt'}, {'Pepper', 'Salt'}])
        {'Garlic', 'Salt', 'Pepper'}
    """
    return set.union(*recipe_sets) if recipe_sets else set()


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    """Remove appetizers from a list of dishes.

    Uses set difference to filter out appetizers from the main dish list.

    Parameters:
        dishes: A list of all dish names.
        appetizers: A list of appetizer names to be removed.

    Returns:
        A list of dishes that are not appetizers.

    Example:
        >>> separate_appetizers(['Salad', 'Steak', 'Bruschetta'], ['Bruschetta', 'Salad'])
        ['Steak']
    """
    appetizer_set = set(appetizers)

    return list(set(dishes) - appetizer_set)


def singleton_ingredients(dishes: list[set[str]], intersection: set[str]) -> set[str]:
    """Identify ingredients that appear in exactly one dish.

    First combines all ingredients from all dishes, then removes ingredients
    that appear in multiple dishes.

    Parameters:
        dishes: A list of sets, where each set contains ingredients for a dish.
        intersection: A set of ingredients that appear in multiple dishes.

    Returns:
        A set of ingredients that appear in exactly one dish.

    Example:
        >>> singleton_ingredients([{'Garlic', 'Onion'}, {'Pepper', 'Garlic'}], {'Garlic'})
        {'Onion', 'Pepper'}
    """
    all_ingredients = set()
    for dish in dishes:
        all_ingredients.update(dish)

    return all_ingredients - intersection