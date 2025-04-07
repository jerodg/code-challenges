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
# todo: Consider what would happen if you run print(replace_word_choice("The cat ate a mouse.", "a", "the")). This would print "The cthet thete the mouse.". Is that what it ought to print? What other unexpected behaviors can be triggered with the right inputs?


def capitalize_title(title: str) -> str:
    """Capitalize the first letter of each word in the title.

    Parameters:
        title: The title string to capitalize.

    Returns:
        A string with the first letter of each word capitalized.

    Example:
        >>> capitalize_title("fish are cold blooded")
        "Fish Are Cold Blooded"
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check if the sentence ends with a period.

    Parameters:
        sentence: The sentence to check.

    Returns:
        True if the sentence ends with a period, False otherwise.

    Example:
        >>> check_sentence_ending("Snails can sleep for 3 years.")
        True
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Remove extra whitespace at the beginning and end of the sentence.

    Parameters:
        sentence: The sentence to clean up.

    Returns:
        A string with leading and trailing whitespace removed.

    Example:
        >>> clean_up_spacing("  Elephants can't jump.  ")
        "Elephants can't jump."
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace all instances of old_word with new_word in the sentence.

    Parameters:
        sentence: The original sentence.
        old_word: The word to be replaced.
        new_word: The replacement word.

    Returns:
        A string with all instances of old_word replaced with new_word.

    Example:
        >>> replace_word_choice("Animals are cool.", "cool", "awesome")
        "Animals are awesome."
    """
    return sentence.replace(old_word, new_word)

