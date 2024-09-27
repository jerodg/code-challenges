"""Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""

import sys
from json import loads


def calculate_common_prefix_lengths(words: list[str], sorted_indices: list[int]) -> list[int]:
    """Calculate the lengths of common prefixes between consecutive words in a sorted list.

    This function iterates through a list of words sorted by their indices and calculates the length
    of the common prefix between each pair of consecutive words. The results are stored in a list
    where each element represents the length of the common prefix for the corresponding word.

    Parameters:
        words (list[str]): The list of words to process.
        sorted_indices (list[int]): The list of indices representing the sorted order of words.

    Returns:
        list[int]: A list of integers representing the lengths of common prefixes between consecutive words.

    Example:
        >>> words = ['apple', 'apricot', 'banana']
        >>> sorted_indices = [0, 1, 2]
        >>> calculate_common_prefix_lengths(words, sorted_indices)
        [0, 2, 0]
    """
    # Initialize a list to store the common prefix lengths, starting with 0 for the first word
    common_prefix_lengths = [0] * len(words)

    # Iterate through the sorted list of words starting from the second word
    for i in range(1, len(words)):
        # Initialize the common length to 0 and determine the maximum possible length of the common prefix
        common_length, max_length = (
            0,
            min(len(prev_word := words[sorted_indices[i - 1]]), len(curr_word := words[sorted_indices[i]])),
        )

        # Increment the common length while the characters of the current and previous words match
        while common_length < max_length and prev_word[common_length] == curr_word[common_length]:
            common_length += 1

        # Store the calculated common length for the current word
        common_prefix_lengths[i] = common_length

    return common_prefix_lengths


def calculate_scores(words: list[str], sorted_indices: list[int], common_prefix_lengths: list[int]) -> list[int]:
    """Calculate the prefix scores for each word in the list.

    This function calculates the prefix scores for each word in the list by iterating through the sorted
    indices and summing the lengths of common prefixes. The scores are updated for each word based on
    the common prefix lengths with subsequent words.

    Parameters:
        words (list[str]): The list of words to process.
        sorted_indices (list[int]): The list of indices representing the sorted order of words.
        common_prefix_lengths (list[int]): The list of common prefix lengths between consecutive words.

    Returns:
        list[int]: A list of integers representing the prefix scores for each word.

    Example:
        >>> words = ['apple', 'apricot', 'banana']
        >>> sorted_indices = [0, 1, 2]
        >>> common_prefix_lengths = [0, 2, 0]
        >>> calculate_scores(words, sorted_indices, common_prefix_lengths)
        [5, 7, 6]
    """
    # Initialize the scores list with zeros, one for each word
    scores = [0] * (n := len(words))

    # Iterate through the sorted indices to calculate scores
    for i, word_index in enumerate(sorted_indices):
        # Start with the length of the current word as the initial score
        scores[word_index] += (common_length := len(words[word_index]))

        # Iterate through subsequent words to update scores based on common prefix lengths
        for j in range(i + 1, n):
            # Update the common length to the minimum of the current common length and the next common prefix length
            if (common_length := min(common_length, common_prefix_lengths[j])) == 0:
                break  # Stop if there is no common prefix

            # Update the scores for the current word and the subsequent word
            scores[word_index] += common_length
            scores[sorted_indices[j]] += common_length

    return scores


def sumPrefixScores(words: list[str]) -> list[int]:
    """Calculate the prefix scores for a list of words.

    This function calculates the prefix scores for each word in the list by first sorting the words
    and then calculating the common prefix lengths between consecutive words. The scores are updated
    based on the common prefix lengths.

    Parameters:
        words (list[str]): The list of words to process.

    Returns:
        list[int]: A list of integers representing the prefix scores for each word.

    Example:
        >>> sumPrefixScores(['apple', 'apricot', 'banana'])
        [5, 7, 6]
    """
    return calculate_scores(
        words,
        sorted_indices := sorted(range(len(words)), key=lambda i: words[i]),
        calculate_common_prefix_lengths(words, sorted_indices),
    )


with open('user.out', 'w', buffering=8192) as sys.stdout:
    # Read JSON input from standard input and process each list of words
    print('\n'.join(sumPrefixScores(words).__str__() for words in map(loads, sys.stdin)).replace(', ', ','))

exit(0)
