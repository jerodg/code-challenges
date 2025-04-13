"""Functions to help Azara and Rui locate pirate treasure.

This module provides utility functions for processing and comparing treasure hunt records
from two different formats (Azara's and Rui's) to help locate pirate treasure.

Azara's records are tuples of (treasure_name, coordinate_string).
Rui's records are tuples of (location_name, coordinate_tuple, quadrant).

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def get_coordinate(record: tuple[str, str]) -> str:
    """Extract the coordinate value from a treasure record.

    This function accesses the second element of a tuple containing treasure
    information, which represents the map coordinate.

    Parameters:
        record: tuple[str, str] - A (treasure_name, coordinate) pair.

    Returns:
        str: The extracted map coordinate.

    Example:
        >>> get_coordinate(("Golden Skull", "2A"))
        "2A"
    """
    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Split the given coordinate string into a tuple of its individual components.

    This function separates a two-character coordinate string into its numeric and
    alphabetic components, returning them as a tuple.

    Parameters:
        coordinate: str - A string map coordinate (e.g. "2A").

    Returns:
        tuple[str, str]: The string coordinate split into its individual components (e.g. ("2", "A")).

    Example:
        >>> convert_coordinate("2A")
        ("2", "A")
    """
    return coordinate[0], coordinate[1]


def compare_records(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> bool:
    """Compare two record types and determine if their coordinates match.

    This function converts Azara's string coordinate into a tuple format
    for comparison with Rui's coordinate tuple.

    Parameters:
        azara_record: tuple[str, str] - A (treasure, coordinate) pair from Azara.
        rui_record: tuple[str, tuple[str, str], str] - A (location, tuple(coordinate_1, coordinate_2), quadrant) trio from Rui.

    Returns:
        bool: True if the coordinates match, False otherwise.

    Example:
        >>> compare_records(("Golden Skull", "2A"), ("Cave", ("2", "A"), "N"))
        True
    """
    azara_coordinate = convert_coordinate(azara_record[1])
    rui_coordinate = rui_record[1]

    return azara_coordinate == rui_coordinate


def create_record(azara_record: tuple[str, str], rui_record: tuple[str, tuple[str, str], str]) -> tuple[str, str, str, tuple[str, str], str] | str:
    """Combine the two record types if their coordinates match.

    This function compares coordinates from Azara's and Rui's records and combines them
    into a single tuple if they match. Otherwise, it returns a failure message.

    Parameters:
        azara_record: tuple[str, str] - A (treasure, coordinate) pair from Azara.
        rui_record: tuple[str, tuple[str, str], str] - A (location, coordinate, quadrant) trio from Rui.

    Returns:
        tuple[str, str, str, tuple[str, str], str] | str: The combined record (if coordinates match),
                                                         or the string "not a match" (if coordinates don't match).

    Example:
        >>> create_record(("Golden Skull", "2A"), ("Cave", ("2", "A"), "N"))
        ("Golden Skull", "2A", "Cave", ("2", "A"), "N")
        >>> create_record(("Golden Skull", "2A"), ("Cave", ("1", "B"), "N"))
        "not a match"
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record

    return "not a match"


def clean_up(combined_record_group: list[tuple]) -> str:
    r"""Format combined records by removing duplicate coordinate information.

    This function processes a list of combined records and removes Azara's coordinate
    from each record to eliminate redundancy in the final output.

    Parameters:
        combined_record_group: list[tuple] - A collection of combined records from both participants.

    Returns:
        str: A multi-line string with each record formatted without Azara's coordinate.

    Example:
        >>> records = [("Golden Skull", "2A", "Cave", ("2", "A"), "N"),
        ...            ("Silver Crown", "3B", "Forest", ("3", "B"), "E")]
        >>> clean_up(records)
        '("Golden Skull", "Cave", ("2", "A"), "N")\n("Silver Crown", "Forest", ("3", "B"), "E")\n'
    """
    result = ""

    for record in combined_record_group:
        # Create a new tuple without Azara's coordinate (index 1)
        cleaned_record = (record[0], record[2], record[3], record[4])
        result += str(cleaned_record) + "\n"

    return result