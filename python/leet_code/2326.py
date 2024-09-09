"""Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see SSPL.
"""

import json
import sys


class ListNode:
    """A node in a singly-linked list.

    This class represents a single node in a singly-linked list, which contains a value and a reference
    to the next node in the list.

    Attributes:
        val (int): The value stored in the node.
        next (ListNode | None): The reference to the next node in the list, or None if this is the last node.
    """

    def __init__(self, val: int = 0, next: 'ListNode' | None = None) -> None:
        """Initializes a ListNode with a given value and next node reference.

        Args:
            val (int): The value to be stored in the node. Defaults to 0.
            next (ListNode | None): The reference to the next node in the list. Defaults to None.
        """
        self.val = val  # Store the value in the node
        self.next = next  # Reference to the next node in the list


class Solution:
    """A class to solve the problem of filling a matrix in a spiral order with values from a linked list.

    This class contains a method to create a matrix of given dimensions and fill it in a spiral order
    using values from a singly-linked list.

    Methods:
        spiralMatrix(rows: int, columns: int, head: ListNode) -> list[list[int]]:
            Fills a matrix in a spiral order with values from a linked list.
    """

    def spiralMatrix(self, rows: int, columns: int, head: ListNode) -> list[list[int]]:
        """Fills a matrix in a spiral order with values from a linked list.

        This method creates a matrix of the specified dimensions and fills it in a spiral order
        using values from the provided singly-linked list. If the list has fewer elements than
        the matrix, the remaining cells are filled with -1.

        Args:
            rows (int): The number of rows in the matrix.
            columns (int): The number of columns in the matrix.
            head (ListNode): The head of the singly-linked list containing the values.

        Returns:
            list[list[int]]: A 2D list representing the matrix filled in a spiral order.

        Example:
            >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
            >>> Solution().spiralMatrix(2, 2, head)
            [[1, 2], [4, 3]]
        """
        # Initialize the matrix with -1 to indicate empty cells
        matrix = [[-1] * columns for _ in range(rows)]

        # Define the boundaries of the spiral traversal
        topRow, bottomRow = 0, rows - 1
        leftColumn, rightColumn = 0, columns - 1

        # Traverse the matrix in a spiral order and fill it with values from the linked list
        while head:
            # Fill the top row from left to right
            for col in range(leftColumn, rightColumn + 1):
                if head:
                    matrix[topRow][col] = head.val
                    head = head.next
            topRow += 1  # Move the top boundary down

            # Fill the right column from top to bottom
            for row in range(topRow, bottomRow + 1):
                if head:
                    matrix[row][rightColumn] = head.val
                    head = head.next
            rightColumn -= 1  # Move the right boundary left

            # Fill the bottom row from right to left
            for col in range(rightColumn, leftColumn - 1, -1):
                if head:
                    matrix[bottomRow][col] = head.val
                    head = head.next
            bottomRow -= 1  # Move the bottom boundary up

            # Fill the left column from bottom to top
            for row in range(bottomRow, topRow - 1, -1):
                if head:
                    matrix[row][leftColumn] = head.val
                    head = head.next
            leftColumn += 1  # Move the left boundary right

        return matrix


def format_output(result: list[list[int]]) -> str:
    """Formats the matrix result into a string representation.

    This function takes a 2D list (matrix) and converts it into a string format suitable for output.
    Each row of the matrix is converted to a string, and all rows are joined with commas and enclosed
    in square brackets.

    Args:
        result (list[list[int]]): The 2D list (matrix) to be formatted.

    Returns:
        str: The string representation of the matrix.

    Example:
        >>> format_output([[1, 2], [3, 4]])
        '[[1,2],[3,4]]'
    """
    # Convert each row of the matrix to a string, remove spaces, and join rows with commas
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'


def main() -> None:
    """Main function to read input, process test cases, and write output.

    This function reads input from standard input, processes multiple test cases to fill matrices
    in a spiral order using values from linked lists, and writes the formatted results to a file.

    The input is expected to be in the following format:
    - Each test case consists of three lines:
        1. The number of rows in the matrix.
        2. The number of columns in the matrix.
        3. A JSON array representing the values in the linked list.

    The function processes each test case, fills the matrix in a spiral order, and writes the
    formatted results to 'user.out'.

    Raises:
        ValueError: If the input format is incorrect or if the JSON array cannot be parsed.

    Example:
        Input:
        2
        2
        [1, 2, 3, 4]
        3
        3
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

        Output in 'user.out':
        [[1,2],[4,3]]
        [[1,2,3],[8,9,4],[7,6,5]]
    """
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()

    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        m = int(lines[i * 3])
        n = int(lines[i * 3 + 1])
        head_values = json.loads(lines[i * 3 + 2])

        if not head_values:
            head = None
        else:
            head = ListNode(head_values[0])
            current = head
            for value in head_values[1:]:
                current.next = ListNode(value)
                current = current.next

        result = Solution().spiralMatrix(m, n, head)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w', encoding='utf-8') as f:
        for result in results:
            f.write(f'{result}\n')


if __name__ == '__main__':
    main()
    sys.exit(0)
