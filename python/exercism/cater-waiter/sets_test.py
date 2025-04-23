"""Exercism Cater Waiter Tests.

Test functions for compiling dishes and ingredients for a catering company.
This module implements various set operations to manage recipe data.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

import unittest

import pytest
from sets import (
    categorize_dish,
    check_drinks,
    clean_ingredients,
    compile_ingredients,
    separate_appetizers,
    singleton_ingredients,
    tag_special_ingredients,
)
from sets_categories_data import KETO, OMNIVORE, PALEO, VEGAN, VEGETARIAN
from sets_test_data import (
    all_drinks,
    dishes_and_appetizers,
    dishes_and_overlap,
    dishes_categorized,
    dishes_cleaned,
    dishes_labeled,
    dishes_to_special_label,
    drink_names,
    ingredients_only,
    recipes_with_duplicates,
    recipes_without_duplicates,
    singletons,
)


class SetsTest(unittest.TestCase):
    """Test suite for the sets module.

    This class tests the functionality of set operations for the catering company's
    recipe management system. It verifies proper handling of ingredients, dish
    categorization, and special dietary considerations.
    """

    @pytest.mark.task(taskno=1)
    def test_clean_ingredients(self) -> None:
        """Test the clean_ingredients function removes duplicate ingredients.

        Verifies that the function converts ingredient lists to sets and pairs
        them with the dish name correctly, eliminating duplicates in the process.
        """
        test_data = zip(recipes_with_duplicates[::3], recipes_without_duplicates[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}", inputs="recipes with duplicated ingredients", result="recipe ingredients de-duped"
            ):
                error_msg = (
                    f"Expected the ingredient list for {item[0]} to be de-duplicated, "
                    "but the ingredients were not cleaned as expected."
                )

                assert clean_ingredients(item[0], item[1]) == (result[1], result[2]), error_msg

    @pytest.mark.task(taskno=2)
    def test_check_drinks(self) -> None:
        """Test the check_drinks function correctly identifies cocktails and mocktails.

        Ensures drinks containing alcoholic ingredients are labeled as cocktails
        and those without are labeled as mocktails.
        """
        test_data = zip(all_drinks[::2], drink_names[::2])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", iputs="all drinks", results="drinks classified"):
                error_msg = f"Expected {result} for {item}, but got something else instead."
                assert check_drinks(item[0], item[1]) == result, error_msg

    @pytest.mark.task(taskno=3)
    def test_categorize_dish(self) -> None:
        """Test the categorize_dish function properly classifies dishes by dietary category.

        Verifies that dishes are correctly categorized as VEGAN, VEGETARIAN, PALEO,
        KETO, or OMNIVORE based on their ingredients.
        """
        test_data = zip(sorted(recipes_without_duplicates, reverse=True)[::3], dishes_categorized[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="categorized dishes"):
                error_message = f"Expected category {result} for {item[0]}, but got a different category instead."
                assert categorize_dish(item[1], item[2]) == result, error_message

    @pytest.mark.task(taskno=4)
    def test_tag_special_ingredients(self) -> None:
        """Test the tag_special_ingredients function identifies special ingredients correctly.

        Confirms that ingredients which are considered "special" are properly
        identified and tagged for each dish.
        """
        test_data = zip(dishes_to_special_label[::3], dishes_labeled[::3])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="all recipes list", results="special ingredients tagged"):
                error_message = f"Expected {result} for {item}, but got something else instead."
                assert tag_special_ingredients(item) == result, error_message

    @pytest.mark.task(taskno=5)
    def test_compile_ingredients(self) -> None:
        """Test the compile_ingredients function combines all ingredients correctly.

        Ensures that all unique ingredients from multiple recipes are properly
        combined into a single comprehensive set.
        """
        test_data = zip(ingredients_only, [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE])

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(
                f"variation #{variant}",
                inputs="all ingredients for all recipes",
                result="combined list of ingredients for all dishes",
            ):
                error_message = "Expected a proper set of combined ingredients, but something went wrong."
                assert compile_ingredients(item) == result, error_message

    @pytest.mark.task(taskno=6)
    def test_separate_appetizers(self) -> None:
        """Test the separate_appetizers function filters out appetizers from the dish list.

        Verifies that the function returns a list of dishes that excludes appetizers
        and maintains the correct return type.
        """
        test_data = zip(dishes_and_appetizers, dishes_cleaned)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="dishes with appetizers", results="appetizers only"):
                error_message = "Expected only appetizers returned, but some dishes remain in the group."
                result_type_error = f"You returned {type(separate_appetizers(item[0], item[1]))}, but a list was expected."
                assert isinstance(separate_appetizers(item[0], item[1]), list), result_type_error
                assert sorted(separate_appetizers(item[0], item[1])) == sorted(result), error_message

    @pytest.mark.task(taskno=7)
    def test_singleton_ingredients(self) -> None:
        """Test the singleton_ingredients function identifies ingredients used in exactly one dish.

        Ensures that the function correctly identifies ingredients that appear in
        only one dish, differentiating them from ingredients used in multiple dishes.
        """
        test_data = zip(dishes_and_overlap, singletons)

        for variant, (item, result) in enumerate(test_data, start=1):
            with self.subTest(f"variation #{variant}", inputs="overlapping ingredients", results="ingredients in only one dish"):
                error_message = "Expected only ingredients that belong to exactly one dish, but got multi-dish ingredients instead."
                assert singleton_ingredients(item[0], item[1]) == result, error_message
