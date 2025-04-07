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

Functions to help edit essay homework using string manipulation.
"""
import unittest

import pytest
from string_methods import capitalize_title, check_sentence_ending, clean_up_spacing, replace_word_choice


class LittleSistersEssayTest(unittest.TestCase):
    """Test suite for the Little Sister's Essay string manipulation functions.

    This test class verifies the functionality of four string manipulation functions:
    - capitalize_title: Capitalizes the first letter of each word in a title
    - check_sentence_ending: Checks if a sentence ends with a period
    - clean_up_spacing: Removes extra whitespace from the beginning and end of a sentence
    - replace_word_choice: Replaces all instances of a specified word in a sentence
    """

    @pytest.mark.task(taskno=1)
    def test_capitalize_word(self) -> None:
        """Test capitalizing a single word.

        Verifies that capitalize_title properly capitalizes the first letter
        of a single-word string.
        """
        actual_result = capitalize_title("canopy")
        expected = "Canopy"
        error_message = (f'Called capitalize_title("canopy"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the title.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=1)
    def test_capitalize_title(self) -> None:
        """Test capitalizing all words in a multi-word title.

        Verifies that capitalize_title properly capitalizes the first letter
        of each word in a multi-word string.
        """
        actual_result = capitalize_title("fish are cold blooded")
        expected = "Fish Are Cold Blooded"
        error_message = (f'Called capitalize_title("fish are cold blooded"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" for the title.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sentence_ending(self) -> None:
        """Test detection of a sentence ending with a period.

        Verifies that check_sentence_ending correctly returns True when
        a sentence ends with a period.
        """
        actual_result = check_sentence_ending("Snails can sleep for 3 years.")
        expected = True
        error_message = (f'Called check_sentence_ending("Snails can sleep for 3 years."). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=2)
    def test_sentence_ending_without_period(self) -> None:
        """Test detection of a sentence not ending with a period.

        Verifies that check_sentence_ending correctly returns False when
        a sentence does not end with a period.
        """
        actual_result = check_sentence_ending("Fittonia are nice")
        expected = False
        error_message = (f'Called check_sentence_ending("Fittonia are nice"). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected} for a period ending.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces_only_start(self) -> None:
        """Test removing leading whitespace from a sentence.

        Verifies that clean_up_spacing correctly removes extra spaces
        from the beginning of a sentence.
        """
        actual_result = clean_up_spacing("  A rolling stone gathers no moss")
        expected = "A rolling stone gathers no moss"
        error_message = (f'Called clean_up_spacing("  A rolling stone gathers no moss"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" as a cleaned string.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=3)
    def test_remove_extra_spaces(self) -> None:
        """Test removing both leading and trailing whitespace from a sentence.

        Verifies that clean_up_spacing correctly removes extra spaces
        from both the beginning and end of a sentence.
        """
        actual_result = clean_up_spacing("  Elephants can't jump.  ")
        expected = "Elephants can't jump."
        error_message = ("Called clean_up_spacing(\"  Elephants can't jump.  \")"
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" as a cleaned string.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_replace_word_choice(self) -> None:
        """Test replacing a word in a sentence.

        Verifies that replace_word_choice correctly replaces all instances
        of a specified word in a sentence with another word.
        """
        actual_result = replace_word_choice("Animals are cool.", "cool", "awesome")
        expected = "Animals are awesome."
        error_message = ('Called replace_word_choice("Animals are cool.", "cool", "awesome"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}" after the word replacement.')

        self.assertEqual(actual_result, expected, msg=error_message)

    @pytest.mark.task(taskno=4)
    def test_replace_word_not_exist(self) -> None:
        """Test replacing a non-existent word in a sentence.

        Verifies that replace_word_choice correctly returns the original
        sentence when the word to be replaced is not present.
        """
        actual_result = replace_word_choice("Animals are cool.", "small", "tiny")
        expected = "Animals are cool."
        error_message = ('Called replace_word_choice("Animals are cool.", "small", "tiny"). '
                         f'The function returned "{actual_result}", '
                         f'but the tests expected "{expected}", because the word '
                         'to be replaced is not in the sentence.')

        self.assertEqual(actual_result, expected, msg=error_message)
