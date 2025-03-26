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

Functions for creating, transforming, and adding prefixes to strings.
"""


def add_prefix_un(word: str) -> str:
    """Add the 'un' prefix to a word.

    Takes a root word and prepends it with the negative prefix 'un', creating
    a new word with opposite meaning.

    Parameters:
        word: The root word to be prefixed.

    Returns:
        The modified word with 'un' prefix attached.

    Example:
        >>> add_prefix_un("happy")
        'unhappy'
        >>> add_prefix_un("manageable")
        'unmanageable'
    """
    return 'un' + word


def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words into a string with prefixed words.

    Takes a list where the first element is a prefix and subsequent elements are root words.
    Creates a string that starts with the prefix followed by each word with the prefix applied,
    all separated by the delimiter ' :: '.

    Parameters:
        vocab_words: A list of strings where the first element is the prefix
                     and remaining elements are words to be prefixed.

    Returns:
        A string containing the prefix and all prefixed words joined with ' :: '.

    Example:
        >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
        'en :: enclose :: enjoy :: enlighten'
        >>> make_word_groups(['pre', 'view', 'dispose'])
        'pre :: preview :: predispose'
    """
    prefix = vocab_words[0]
    result = [prefix]

    result.extend(prefix + word for word in vocab_words[1:])

    return ' :: '.join(result)


def remove_suffix_ness(word: str) -> str:
    """Remove the 'ness' suffix from a word and adjust spelling.

    Takes a word ending with 'ness' and removes this suffix. If the resulting
    root word ends with 'i', converts it to 'y' to maintain correct spelling.

    Parameters:
        word: A string ending with the suffix 'ness'.

    Returns:
        The root word with suffix removed and spelling adjusted.

    Example:
        >>> remove_suffix_ness("heaviness")
        'heavy'
        >>> remove_suffix_ness("sadness")
        'sad'
    """
    root = word[:-4]  # Remove 'ness'

    # If the root ends with 'i', change it back to 'y'
    if root.endswith('i'):
        root = root[:-1] + 'y'

    return root


def adjective_to_verb(sentence: str, index: int) -> str:
    """Convert an adjective from a sentence into a verb.

    Extracts a word at the specified index from the sentence and transforms it
    into a verb by adding the suffix 'en'. Any punctuation at the end of the
    word is removed before adding the suffix.

    Parameters:
        sentence: A string containing the adjective to be converted.
        index: The position of the adjective in the sentence (zero-indexed).

    Returns:
        The adjective converted to a verb form by adding 'en'.

    Example:
        >>> adjective_to_verb("It got dark as the sun set.", 2)
        'darken'
        >>> adjective_to_verb("The water was clear.", 2)
        'clearen'
    """
    words = sentence.split()
    adjective = words[index]

    # Remove punctuation if present
    if not adjective[-1].isalnum():
        adjective = adjective[:-1]

    return adjective + 'en'
