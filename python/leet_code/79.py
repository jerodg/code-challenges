"""
Module for finding if a word exists in a 2D grid of characters.

This module provides a solution for finding if a word exists in a 2D grid of characters.
The solution is implemented in the `Solution` class, which has a method `exist`. This method takes a 2D list of characters
representing the grid and a string representing the word to be found and returns a boolean indicating if the word exists in the grid.

Example:
    >>> s = Solution()
    >>> board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    >>> word = 'ABCCED'
    >>> print(s.exist(board, word))
    True

This module requires Python 3.12 or later.

Author:
    Jerod Gawne (https://github.com/jerodg)

Date:
    2024.1
"""

from typing import List


class Solution:
    """
    This class provides a solution to the problem of finding if a word exists in a 2D grid of characters.
    """

    def dfs(self, board: List[List[str]], i: int, j: int, word: str, index: int) -> bool:
        """
        This function performs a depth-first search on the grid to find the word.

        Args:
            board (List[List[str]]): A 2D list of characters representing the grid.
            i (int): The row index.
            j (int): The column index.
            word (str): The word to be found.
            index (int): The index of the character in the word to be found.

        Returns:
            bool: True if the word exists in the grid, False otherwise.

        Raises:
            IndexError: If `i` or `j` is out of bounds.

        Example:
            >>> s = Solution()
            >>> board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
            >>> word = 'ABCCED'
            >>> print(s.dfs(board, 0, 0, word, 0))
            True
        """
        # Check if the index is equal to the length of the word
        if index == len(word):
            return True

        # Check if the row and column are out of bounds
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        # Check if the character in the board is not equal to the character in the word
        if board[i][j] != word[index]:
            return False

        # Store the character in the board
        temp = board[i][j]

        # Mark the character as visited
        board[i][j] = '.'

        # Check if the word exists in the board
        if (
            self.dfs(board, i + 1, j, word, index + 1)
            or self.dfs(board, i - 1, j, word, index + 1)
            or self.dfs(board, i, j + 1, word, index + 1)
            or self.dfs(board, i, j - 1, word, index + 1)
        ):
            return True

        # Restore the character in the board
        board[i][j] = temp

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        This function checks if a word exists in a 2D grid of characters.

        Args:
            board (List[List[str]]): A 2D list of characters representing the grid.
            word (str): The word to be found.

        Returns:
            bool: True if the word exists in the grid, False otherwise.

        Raises:
            ValueError: If `board` is not a 2D list or `word` is not a string.

        Example:
            >>> s = Solution()
            >>> board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
            >>> word = 'ABCCED'
            >>> print(s.exist(board, word))
            True

            >>> word = 'SEE'
            >>> print(s.exist(board, word))
            True

            >>> word = 'ABCB'
            >>> print(s.exist(board, word))
            False
        """
        if not isinstance(board, list) or not all(isinstance(row, list) for row in board) or not isinstance(word, str):
            raise ValueError('`board` must be a 2D list and `word` must be a string.')

        # Iterate over the rows in the board
        for i in range(len(board)):
            # Iterate over the columns in the board
            for j in range(len(board[0])):
                # If the character in the board is the same as the first character
                # in the word, then check if the word exists in the board
                if board[i][j] == word[0] and self.dfs(board, i, j, word, 0):
                    return True
        return False
