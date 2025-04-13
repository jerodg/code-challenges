"""Test Functions to help Azara and Rui locate pirate treasure.

This module provides utility functions for processing and comparing treasure hunt records
from two different formats (Azara's and Rui's) to help locate pirate treasure.

Azara's records are tuples of (treasure_name, coordinate_string).
Rui's records are tuples of (location_name, coordinate_tuple, quadrant).

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

import unittest

import pytest
from tuples import clean_up, compare_records, convert_coordinate, create_record, get_coordinate


class TisburyTreasureTest(unittest.TestCase):
    """Test suite for the treasure hunt utility functions.

    This test class validates the functionality of the helper functions that process
    and compare treasure hunt records from Azara and Rui to locate pirate treasure.
    Each test method corresponds to a specific task in the assignment.
    """

    @pytest.mark.task(taskno=1)
    def test_get_coordinate(self) -> None:
        """Test the get_coordinate function extracts coordinates correctly from records.

        Verifies that the function can extract the second element (coordinate) from
        a tuple containing treasure information.
        """
        input_data = [
            ("Scrimshawed Whale Tooth", "2A"),
            ("Brass Spyglass", "4B"),
            ("Robot Parrot", "1C"),
            ("Glass Starfish", "6D"),
            ("Vintage Pirate Hat", "7E"),
            ("Pirate Flag", "7F"),
            ("Crystal Crab", "6A"),
            ("Model Ship in Large Bottle", "8A"),
            ("Angry Monkey Figurine", "5B"),
            ("Carved Wooden Elephant", "8C"),
            ("Amethyst  Octopus", "1F"),
            ("Antique Glass Fishnet Float", "3D"),
            ("Silver Seahorse", "4E"),
        ]

        result_data = ["2A", "4B", "1C", "6D", "7E", "7F", "6A", "8A", "5B", "8C", "1F", "3D", "4E"]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", item=item, expected=expected):
                actual_result = get_coordinate(item)
                error_message = (
                    f"Called get_coordinate({item}). "
                    f'The function returned "{actual_result}", but '
                    f'the tests expected "{expected}" as the coordinates.'
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=2)
    def test_convert_coordinate(self) -> None:
        """Test the convert_coordinate function properly splits coordinate strings.

        Verifies that the function correctly splits a string coordinate (e.g. "2A")
        into a tuple of individual components (e.g. ("2", "A")).
        """
        input_data = ["2A", "4B", "1C", "6D", "7E", "7F", "6A", "8A", "5B", "8C", "1F", "3D", "4E"]
        result_data = [
            ("2", "A"),
            ("4", "B"),
            ("1", "C"),
            ("6", "D"),
            ("7", "E"),
            ("7", "F"),
            ("6", "A"),
            ("8", "A"),
            ("5", "B"),
            ("8", "C"),
            ("1", "F"),
            ("3", "D"),
            ("4", "E"),
        ]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", item=item, expected=expected):
                actual_result = convert_coordinate(item)
                error_message = (
                    f"Called convert_coordinate({item}). "
                    f"The function returned {actual_result}, but the "
                    f"tests expected {expected} as the converted coordinate."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_compare_records(self) -> None:
        """Test the compare_records function correctly compares coordinates from different record formats.

        Verifies that the function accurately determines whether Azara's string coordinate
        matches Rui's tuple coordinate when converted to the same format.
        """
        input_data = [
            (("Scrimshawed Whale Tooth", "2A"), ("Deserted Docks", ("2", "A"), "Blue")),
            (("Brass Spyglass", "4B"), ("Abandoned Lighthouse", ("4", "B"), "Blue")),
            (("Robot Parrot", "1C"), ("Seaside Cottages", ("1", "C"), "Blue")),
            (("Glass Starfish", "6D"), ("Tangled Seaweed Patch", ("6", "D"), "Orange")),
            (("Vintage Pirate Hat", "7E"), ("Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange")),
            (("Amethyst  Octopus", "1F"), ("Seaside Cottages", ("1", "C"), "Blue")),
            (("Angry Monkey Figurine", "5B"), ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow")),
            (("Antique Glass Fishnet Float", "3D"), ("Deserted Docks", ("2", "A"), "Blue")),
            (("Brass Spyglass", "4B"), ("Spiky Rocks", ("3", "D"), "Yellow")),
            (("Carved Wooden Elephant", "8C"), ("Abandoned Lighthouse", ("4", "B"), "Blue")),
        ]
        result_data = [True, True, True, True, True, False, False, False, False, False]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", item=item, expected=expected):
                actual_result = compare_records(item[0], item[1])
                error_message = (
                    f"Called compare_records({item[0]}, {item[1]}). "
                    f"The function returned {actual_result}, but the "
                    f"tests expected {expected}."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_create_record(self) -> None:
        """Test the create_record function properly combines matching records.

        Verifies that the function combines Azara's and Rui's records into a single tuple
        when their coordinates match, or returns "not a match" when they don't.
        """
        input_data = [
            (("Angry Monkey Figurine", "5B"), ("Stormy Breakwater", ("5", "B"), "Purple")),
            (("Carved Wooden Elephant", "8C"), ("Foggy Seacave", ("8", "C"), "Purple")),
            (("Amethyst  Octopus", "1F"), ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow")),
            (("Antique Glass Fishnet Float", "3D"), ("Spiky Rocks", ("3", "D"), "Yellow")),
            (("Silver Seahorse", "4E"), ("Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow")),
            (("Amethyst  Octopus", "1F"), ("Seaside Cottages", ("1", "C"), "Blue")),
            (("Angry Monkey Figurine", "5B"), ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow")),
            (("Antique Glass Fishnet Float", "3D"), ("Deserted Docks", ("2", "A"), "Blue")),
            (("Brass Spyglass", "4B"), ("Spiky Rocks", ("3", "D"), "Yellow")),
            (("Carved Wooden Elephant", "8C"), ("Abandoned Lighthouse", ("4", "B"), "Blue")),
        ]
        result_data = [
            ("Angry Monkey Figurine", "5B", "Stormy Breakwater", ("5", "B"), "Purple"),
            ("Carved Wooden Elephant", "8C", "Foggy Seacave", ("8", "C"), "Purple"),
            ("Amethyst  Octopus", "1F", "Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
            ("Antique Glass Fishnet Float", "3D", "Spiky Rocks", ("3", "D"), "Yellow"),
            ("Silver Seahorse", "4E", "Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
            "not a match",
            "not a match",
            "not a match",
            "not a match",
            "not a match",
        ]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", item=item, expected=expected):
                actual_result = create_record(item[0], item[1])
                error_message = (
                    f"Called create_record({item[0]},{item[1]}). "
                    f"The function returned "
                    f"{actual_result}, but the tests expected "
                    f"{expected} for the record."
                )

                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=5)
    def test_clean_up(self) -> None:
        """Test the clean_up function correctly formats the combined records.

        Verifies that the function removes redundant coordinate information from
        combined records and formats them as a multi-line string with each record
        presented in a standardized format.
        """
        input_data = (
            ("Scrimshawed Whale Tooth", "2A", "Deserted Docks", ("2", "A"), "Blue"),
            ("Brass Spyglass", "4B", "Abandoned Lighthouse", ("4", "B"), "Blue"),
            ("Robot Parrot", "1C", "Seaside Cottages", ("1", "C"), "Blue"),
            ("Glass Starfish", "6D", "Tangled Seaweed Patch", ("6", "D"), "Orange"),
            ("Vintage Pirate Hat", "7E", "Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
            ("Pirate Flag", "7F", "Windswept Hilltop (Island of Mystery)", ("7", "F"), "Orange"),
            ("Crystal Crab", "6A", "Old Schooner", ("6", "A"), "Purple"),
            ("Model Ship in Large Bottle", "8A", "Harbor Managers Office", ("8", "A"), "Purple"),
            ("Angry Monkey Figurine", "5B", "Stormy Breakwater", ("5", "B"), "Purple"),
            ("Carved Wooden Elephant", "8C", "Foggy Seacave", ("8", "C"), "Purple"),
            ("Amethyst  Octopus", "1F", "Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
            ("Antique Glass Fishnet Float", "3D", "Spiky Rocks", ("3", "D"), "Yellow"),
            ("Silver Seahorse", "4E", "Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
        )

        result_data = """('Scrimshawed Whale Tooth', 'Deserted Docks', ('2', 'A'), 'Blue')\n\
    ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n\
    ('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')\n\
    ('Glass Starfish', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange')\n\
    ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n\
    ('Pirate Flag', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange')\n\
    ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n\
    ('Model Ship in Large Bottle', 'Harbor Managers Office', ('8', 'A'), 'Purple')\n\
    ('Angry Monkey Figurine', 'Stormy Breakwater', ('5', 'B'), 'Purple')\n\
    ('Carved Wooden Elephant', 'Foggy Seacave', ('8', 'C'), 'Purple')\n\
    ('Amethyst  Octopus', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')\n\
    ('Antique Glass Fishnet Float', 'Spiky Rocks', ('3', 'D'), 'Yellow')\n\
    ('Silver Seahorse', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"""

        assert clean_up(input_data) == result_data
