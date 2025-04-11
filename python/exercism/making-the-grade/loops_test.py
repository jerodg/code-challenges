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

Test functions for organizing and calculating student exam scores.
"""

import unittest

import pytest
from loops import above_threshold, count_failed_students, letter_grades, perfect_score, round_scores, student_ranking


class MakingTheGradeTest(unittest.TestCase):
    """Unit tests for functions related to organizing and calculating student exam scores."""

    @pytest.mark.task(taskno=1)
    def test_round_scores(self) -> None:
        """Test the `round_scores` function.

        Verifies that the function correctly rounds a list of student scores to the nearest integer.

        Test Cases:
            - Empty input list.
            - Single-element lists with scores requiring rounding.
            - Multi-element lists with scores requiring rounding.

        Asserts:
            - The rounded scores match the expected results.
        """
        test_data = [
            (),
            (0.5,),
            (1.5,),
            (90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3),
            (50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0),
        ]
        result_data = [[], [0], [2], [90, 40, 55, 70, 31, 25, 80, 95, 39, 40], [50, 36, 77, 41, 43, 78, 64, 91, 29, 88]]

        for variant, (student_scores, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", student_scores=student_scores, expected=expected):
                actual_result = round_scores(list(student_scores))
                error_message = (
                    f"Called round_scores({list(student_scores)}). "
                    f"The function returned {sorted(actual_result)} after sorting, but "
                    f"the tests expected {sorted(expected)} after sorting. "
                    f"One or more scores were rounded incorrectly."
                )
                assert sorted(actual_result) == sorted(expected), error_message

    @pytest.mark.task(taskno=2)
    def test_count_failed_students(self) -> None:
        """Test the `count_failed_students` function.

        Verifies that the function correctly counts the number of students who failed
        (scores less than or equal to 40).

        Test Cases:
            - Lists with no failing students.
            - Lists with multiple failing students.

        Asserts:
            - The count of failing students matches the expected results.
        """
        test_data = [[89, 85, 42, 57, 90, 100, 95, 48, 70, 96], [40, 40, 35, 70, 30, 41, 90]]
        result_data = [0, 4]

        for variant, (student_scores, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", student_scores=student_scores, expected=expected):
                actual_result = count_failed_students(student_scores)
                error_message = (
                    f"Called count_failed_students({student_scores}). "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} for the "
                    "number of students who failed."
                )
                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=3)
    def test_above_threshold(self) -> None:
        """Test the `above_threshold` function.

        Verifies that the function correctly filters scores that are above a given threshold.

        Test Cases:
            - Lists with no scores above the threshold.
            - Lists with multiple scores above the threshold.
            - Empty input list.

        Asserts:
            - The filtered scores match the expected results.
        """
        test_data = [
            ([40, 39, 95, 80, 25, 31, 70, 55, 40, 90], 98),
            ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80),
            ([100, 89], 100),
            ([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 78),
            ([], 80),
        ]
        result_data = [[], [88, 91], [100], [88, 91, 78], []]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = above_threshold(*params)
                error_message = (
                    f"Called above_threshold{params}. "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} for the "
                    "scores that are above the threshold."
                )
                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=4)
    def test_letter_grades(self) -> None:
        """Test the `letter_grades` function.

        Verifies that the function correctly calculates the thresholds for letter grades
        based on the highest score.

        Test Cases:
            - Different highest scores to verify correct interval calculation.

        Asserts:
            - The calculated grade thresholds match the expected results.
        """
        test_data = [100, 97, 85, 92, 81]
        result_data = [[41, 56, 71, 86], [41, 55, 69, 83], [41, 52, 63, 74], [41, 54, 67, 80], [41, 51, 61, 71]]

        for variant, (highest, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", highest=highest, expected=expected):
                actual_result = letter_grades(highest)
                error_message = (
                    f"Called letter_grades({highest}). "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} for the "
                    "letter grade cutoffs."
                )
                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=5)
    def test_student_ranking(self) -> None:
        """Test the `student_ranking` function.

        Verifies that the function correctly generates a formatted list of student rankings
        based on their scores.

        Test Cases:
            - Single student.
            - Multiple students with varying scores.

        Asserts:
            - The formatted rankings match the expected results.
        """
        test_data = [
            ([82], ["Betty"]),
            ([88, 73], ["Paul", "Ernest"]),
            ([100, 98, 92, 86, 70, 68, 67, 60], ["Rui", "Betty", "Joci", "Yoshi", "Kora", "Bern", "Jan", "Rose"]),
        ]
        result_data = [
            ["1. Betty: 82"],
            ["1. Paul: 88", "2. Ernest: 73"],
            [
                "1. Rui: 100",
                "2. Betty: 98",
                "3. Joci: 92",
                "4. Yoshi: 86",
                "5. Kora: 70",
                "6. Bern: 68",
                "7. Jan: 67",
                "8. Rose: 60",
            ],
        ]

        for variant, (params, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", params=params, expected=expected):
                actual_result = student_ranking(*params)
                error_message = (
                    f"Called student_ranking{params}. "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} for the "
                    "student rankings."
                )
                assert actual_result == expected, error_message

    @pytest.mark.task(taskno=6)
    def test_perfect_score(self) -> None:
        """Test the `perfect_score` function.

        Verifies that the function correctly identifies the first student with a perfect score (100).

        Test Cases:
            - Lists with multiple perfect scores.
            - Lists with no perfect scores.
            - Empty input list.

        Asserts:
            - The first student with a perfect score matches the expected result.
        """
        test_data = [
            [["Joci", 100], ["Vlad", 100], ["Raiana", 100], ["Alessandro", 100]],
            [["Jill", 30], ["Paul", 73]],
            [],
            [
                ["Rui", 60],
                ["Joci", 58],
                ["Sara", 91],
                ["Kora", 93],
                ["Alex", 42],
                ["Jan", 81],
                ["Lilliana", 40],
                ["John", 60],
                ["Bern", 28],
                ["Vlad", 55],
            ],
            [["Yoshi", 52], ["Jan", 86], ["Raiana", 100], ["Betty", 60], ["Joci", 100], ["Kora", 81], ["Bern", 41], ["Rose", 94]],
        ]
        result_data = [["Joci", 100], [], [], [], ["Raiana", 100]]

        for variant, (student_info, expected) in enumerate(zip(test_data, result_data), start=1):
            with self.subTest(f"variation #{variant}", student_info=student_info, expected=expected):
                actual_result = perfect_score(student_info)
                error_message = (
                    f"Called perfect_score({student_info}). "
                    f"The function returned {actual_result}, but "
                    f"the tests expected {expected} for the "
                    'first "perfect" score.'
                )
                assert actual_result == expected, error_message
