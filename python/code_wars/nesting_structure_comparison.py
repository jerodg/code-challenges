"""CodeWars Nesting Structure Comparison.

Provides functionality to compare two nested structures (lists and dictionaries)

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def same_structure_as(original, other) -> bool:
    """Compare if two structures have the same nesting pattern.

    Parameters:
        original: First structure to compare
        other: Second structure to compare

    Returns:
        bool: True if both structures have the same nesting pattern, False otherwise

    Examples:
        >>> same_structure_as([1, 1, 1], [2, 2, 2])
        True
        >>> same_structure_as([1, [1, 1]], [2, [2, 2]])
        True
        >>> same_structure_as([1, [1, 1]], [[2, 2], 2])
        False
    """
    # Check if both are lists
    if isinstance(original, list) and isinstance(other, list):
        # Check if they have the same length
        if len(original) != len(other):
            return False

        # Check each element recursively
        for i in range(len(original)):
            # If one is a list and the other is not, structures don't match
            if isinstance(original[i], list) != isinstance(other[i], list):
                return False

            # If both are lists, compare them recursively
            if isinstance(original[i], list) and not same_structure_as(original[i], other[i]):
                return False

        # If we've made it here, structures match
        return True

    # If one is a list and the other is not, structures don't match
    if isinstance(original, list) or isinstance(other, list):
        return False

    # If neither is a list, they are just values and have the same structure
    return True
