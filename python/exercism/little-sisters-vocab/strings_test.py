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

import unittest

import pytest
from strings import add_prefix_un, adjective_to_verb, make_word_groups, remove_suffix_ness


class LittleSistersVocabTest(unittest.TestCase):
    """Test suite for Little Sister's Vocabulary functions.

    This test class verifies the functionality of string manipulation
    functions used in the Little Sister's Vocabulary exercise, including
    prefix addition, word group creation, suffix removal, and adjective-to-verb
    transformation.
    """

    @pytest.mark.task(taskno=1)
    def test_add_prefix_un(self) -> None:
        """Test the add_prefix_un function with various words.

        Verifies that the function correctly prepends 'un' to different root words.
        """
        input_data = ['happy', 'manageable', 'fold', 'eaten', 'avoidable', 'usual']
        result_data = [f'un{item}' for item in input_data]

        for variant, (word, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', word=word, expected=expected):
                actual_result = add_prefix_un(word)
                error_message = (
                    f'Called add_prefix_un("{word}"). '
                    f'The function returned "{actual_result}", but the '
                    f'tests expected "{expected}" after adding "un" as a prefix.'
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_en(self) -> None:
        """Test the make_word_groups function with the 'en' prefix.

        Ensures the function correctly joins a list starting with 'en' prefix
        and applies the prefix to each subsequent word in the expected format.
        """
        input_data = ['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture']
        expected = 'en :: encircle :: enfold :: enclose :: enjoy :: enlighten :: entangle :: enable :: encode :: enculture'

        actual_result = make_word_groups(input_data)
        error_message = (
            f'Called make_word_groups({input_data}). '
            f'The function returned "{actual_result}", '
            f'but the tests expected "{expected}" for the '
            'word groups.'
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_pre(self) -> None:
        """Test the make_word_groups function with the 'pre' prefix.

        Verifies that the function correctly handles words prefixed with 'pre'
        and formats the output string properly.
        """
        input_data = [
            'pre',
            'serve',
            'dispose',
            'position',
            'requisite',
            'digest',
            'natal',
            'addressed',
            'adolescent',
            'assumption',
            'mature',
            'compute',
        ]
        expected = (
            'pre :: preserve :: predispose :: preposition :: prerequisite :: '
            'predigest :: prenatal :: preaddressed :: preadolescent :: preassumption :: '
            'premature :: precompute'
        )

        actual_result = make_word_groups(input_data)
        error_message = (
            f'Called make_word_groups({input_data}). '
            f'The function returned "{actual_result}", '
            f'but the tests expected "{expected}" for the '
            'word groups.'
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_make_word_groups_auto(self) -> None:
        """Test the make_word_groups function with the 'auto' prefix.

        Checks that the function correctly applies the 'auto' prefix to
        various words and formats the result string as expected.
        """
        input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete', 'echolalia', 'encoder', 'biography']
        expected = (
            'auto :: autodidactic :: autograph :: automate :: autochrome :: '
            'autocentric :: autocomplete :: autoecholalia :: autoencoder :: '
            'autobiography'
        )

        actual_result = make_word_groups(input_data)
        error_message = (
            f'Called make_word_groups({input_data}). '
            f'The function returned "{actual_result}", '
            f'but the tests expected "{expected}" for the '
            'word groups.'
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_make_words_groups_inter(self) -> None:
        """Test the make_word_groups function with the 'inter' prefix.

        Verifies the function correctly processes words with the 'inter' prefix
        and produces the expected output string format.
        """
        input_data = [
            'inter',
            'twine',
            'connected',
            'dependent',
            'galactic',
            'action',
            'stellar',
            'cellular',
            'continental',
            'axial',
            'operative',
            'disciplinary',
        ]
        expected = (
            'inter :: intertwine :: interconnected :: interdependent :: '
            'intergalactic :: interaction :: interstellar :: intercellular :: '
            'intercontinental :: interaxial :: interoperative :: interdisciplinary'
        )

        actual_result = make_word_groups(input_data)
        error_message = (
            f'Called make_word_groups({input_data}). '
            f'The function returned "{actual_result}", '
            f'but the tests expected "{expected}" for the '
            'word groups.'
        )

        assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_remove_suffix_ness(self) -> None:
        """Test the remove_suffix_ness function with various words.

        Checks that the function correctly removes the 'ness' suffix and
        makes appropriate spelling adjustments (i.e., 'i' to 'y' when needed).
        """
        input_data = ['heaviness', 'sadness', 'softness', 'crabbiness', 'lightness', 'artiness', 'edginess']
        result_data = ['heavy', 'sad', 'soft', 'crabby', 'light', 'arty', 'edgy']

        for variant, (word, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', word=word, expected=expected):
                actual_result = remove_suffix_ness(word)
                error_message = (
                    f'Called remove_suffix_ness("{word}"). '
                    f'The function returned "{actual_result}", '
                    f'but the tests expected "{expected}" after the '
                    'suffix was removed.'
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_adjective_to_verb(self) -> None:
        """Test the adjective_to_verb function with various sentences.

        Verifies that the function correctly extracts an adjective from
        a sentence at the specified index, removes any punctuation, and
        converts it to a verb by adding the 'en' suffix.
        """
        input_data = [
            'Look at the bright sky.',
            'His expression went dark.',
            'The bread got hard after sitting out.',
            'The butter got soft in the sun.',
            'Her eyes were light blue.',
            'The morning fog made everything damp with mist.',
            'He cut the fence pickets short by mistake.',
            'Charles made weak crying noises.',
            'The black oil got on the white dog.',
        ]
        index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]
        result_data = ['brighten', 'darken', 'harden', 'soften', 'lighten', 'dampen', 'shorten', 'weaken', 'blacken']

        for variant, (sentence, index, expected) in enumerate(zip(input_data, index_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', sentence=sentence, index=index, expected=expected):
                actual_result = adjective_to_verb(sentence, index)
                error_message = (
                    f'Called adjective_to_verb("{sentence}", {index}). '
                    f'The function returned "{actual_result}", but the tests '
                    f'expected "{expected}" as the verb for '
                    f'the word at index {index}.'
                )

                assert actual_result == expected, error_message
