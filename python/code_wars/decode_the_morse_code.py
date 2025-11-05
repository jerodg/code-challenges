"""Code Wars Decode the Morse Code.

This module provides functionality to decode Morse code strings into human-readable text.
It handles standard Morse code encoding with single spaces separating characters and triple spaces separating words.
Extra leading or trailing spaces are ignored, and the decoding relies on a preloaded MORSE_CODE dictionary.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

from preloaded import MORSE_CODE


def decode_morse(morse_code: str) -> str:
    """Decode a Morse code string into human-readable text.

    Processes the input by removing extraneous spaces, splitting into words and characters,
    and mapping each Morse symbol to its corresponding letter or digit using the MORSE_CODE dictionary.
    This approach ensures accurate decoding while handling variable spacing in the input.

    Parameters:
        morse_code: The Morse code string to decode, with characters separated by single spaces
            and words by triple spaces.

    Returns:
        The decoded string in uppercase, with words separated by single spaces.

    Raises:
        KeyError: If an unrecognized Morse symbol is encountered in the input.

    Example:
        >>> decode_morse('.... . -.--   .--- ..- -.. .')
        'HEY JUDE'
    """
    # Strip leading and trailing spaces to normalize input and avoid empty splits.
    morse_code = morse_code.strip()
    # Split on triple spaces to isolate words, as this delimiter indicates word boundaries.
    words = morse_code.split('   ')
    # Initialize list to collect decoded words for efficient joining later.
    decoded_words = []
    for word in words:
        # Split on single spaces to isolate individual Morse characters within the word.
        letters = word.split()
        # Decode each Morse symbol to its letter/digit; list comprehension used for conciseness.
        decoded_letters = [MORSE_CODE[letter] for letter in letters]
        # Join decoded letters into a word string.
        decoded_words.append(''.join(decoded_letters))
    # Join decoded words with single spaces to form the final readable string.
    return ' '.join(decoded_words)
