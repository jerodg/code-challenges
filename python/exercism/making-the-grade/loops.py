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

Functions for organizing and calculating student exam scores.
"""


def round_scores(student_scores: list[float]) -> list[int]:
    """Round a list of student scores to the nearest integer.

    This function modifies the input list in-place while creating a new list of
    rounded scores.

    Parameters:
        student_scores: A list of floating-point student scores

    Returns:
        A new list containing the rounded scores

    Example:
        >>> round_scores([90.33, 40.5, 55.44, 70.05])
        [90, 41, 55, 70]
    """
    rounded_scores = []
    while student_scores:
        rounded_scores.append(round(student_scores.pop(0)))

    return rounded_scores


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students.

    A student fails if their score is less than or equal to 40.

    Parameters:
        student_scores: A list of student scores

    Returns:
        The count of students who failed

    Example:
        >>> count_failed_students([40, 40, 35, 70, 30, 41, 90])
        4
    """
    failed_count = 0
    for score in student_scores:
        if score <= 40:
            failed_count += 1

    return failed_count


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Filter scores that are at or above a specified threshold.

    Parameters:
        student_scores: A list of student scores
        threshold: The minimum score to be included in the result

    Returns:
        A list containing only the scores that are greater than or equal to the threshold

    Example:
        >>> above_threshold([88, 29, 91, 64, 78, 43, 41, 77, 36, 50], 80)
        [88, 91]
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Calculate the thresholds for letter grades based on the highest score.

    Using the highest score, creates a list of lower thresholds for each letter grade:
    - 'D' threshold: 41 (just above failing)
    - 'C' threshold: 41 + interval
    - 'B' threshold: 41 + 2*interval
    - 'A' threshold: 41 + 3*interval

    Where interval is the equal distribution between the failing threshold (40)
    and the highest score, divided into 4 letter grades.

    Parameters:
        highest: The highest score in the class

    Returns:
        A list of score thresholds for letter grades D, C, B, and A

    Example:
        >>> letter_grades(100)
        [41, 56, 71, 86]
    """
    failing_threshold = 40  # The score below which students fail
    interval = (highest - failing_threshold) // 4  # Calculate the interval for grade thresholds

    return [
        failing_threshold + 1,  # Threshold for grade 'D'
        failing_threshold + 1 + interval,  # Threshold for grade 'C'
        failing_threshold + 1 + (2 * interval),  # Threshold for grade 'B'
        failing_threshold + 1 + (3 * interval),  # Threshold for grade 'A'
    ]


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Create a formatted list of student rankings with names and scores.

    Combines student names with their corresponding scores and adds a ranking number.

    Parameters:
        student_scores: A list of student scores.
        student_names: A list of student names.

    Returns:
        A list of formatted strings showing the ranking, name, and score for each student.

    Example:
        >>> student_ranking([88, 73], ["Paul", "Ernest"])
        ['1. Paul: 88', '2. Ernest: 73']
    """
    ranking_list = []  # Initialize an empty list to store the rankings.
    for i, (name, score) in enumerate(zip(student_names, student_scores), 1):
        # Combine the rank, name, and score into a formatted string and append to the list.
        ranking_list.append(f"{i}. {name}: {score}")

    return ranking_list


def perfect_score(student_info: list[list[str, int]] | list[tuple[str, int]]) -> list[str, int] | list:
    """Find the first student with a perfect score.

    Iterates through a list of student information to find the first student
    who has a score of 100. Each student is represented as a list or tuple
    where the second element is their score.

    Parameters:
        student_info: A list of lists or tuples, where each contains a student's
                      name and score (e.g., ["John", 100]).

    Returns:
        The first student (list or tuple) with a score of 100, or an empty list
        if no such student is found.

    Example:
        >>> perfect_score([["Alice", 99], ["Bob", 100], ["Charlie", 98]])
        ["Bob", 100]
    """
    for student in student_info:
        if student[1] == 100:
            return student

    return []
