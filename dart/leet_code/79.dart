/// Dart implementation of the LeetCode problem 79: Word Search.
///
/// This module contains a class `Solution` with two methods: `dfs` and `exist`.
/// The `dfs` method is a helper function used by the `exist` method.
///
/// The `exist` method takes in two parameters:
/// - `board`: A 2D list of strings representing the word board.
/// - `word`: A string representing the word to be searched in the board.
///
/// The method returns a boolean indicating whether the word can be found in the board by moving up, down, left, or right from a cell.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `board` is a 2D list of strings and `word` is a string.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.
library;

import 'dart:core';

class Solution {
  /// Helper function to perform depth-first search on the board.
  ///
  /// This method takes in five parameters:
  /// - `board`: The word board.
  /// - `i` and `j`: The current position in the board.
  /// - `word`: The word to be searched.
  /// - `k`: The current position in the word.
  ///
  /// The method returns a boolean indicating whether the word can be found starting from the current position.
  bool dfs(List<List<String>> board, int i, int j, String word, int k) {
    // If the current position is out of bounds or the current character does not match the word, return false.
    if (i < 0 || j < 0 || i >= board.length || j >= board[i].length || board[i][j] != word[k]) return false;

    // If the entire word has been found, return true.
    if (k == word.length - 1) return true;

    // Temporarily mark the current position as visited.
    var temp = board[i][j];
    board[i][j] = '';

    // Recursively search in the four adjacent directions.
    if (dfs(board, i + 1, j, word, k + 1) ||
        dfs(board, i - 1, j, word, k + 1) ||
        dfs(board, i, j + 1, word, k + 1) ||
        dfs(board, i, j - 1, word, k + 1)) {
      return true;
    }

    // Restore the current position.
    board[i][j] = temp;

    // If the word cannot be found starting from the current position, return false.
    return false;
  }

  /// Determines whether the word can be found in the board by moving up, down, left, or right from a cell.
  ///
  /// This method uses the helper function `dfs` to perform depth-first search on the board.
  ///
  /// @param board The word board.
  /// @param word The word to be searched.
  /// @return A boolean indicating whether the word can be found in the board.
  bool exist(List<List<String>> board, String word) {
    // Traverse the board.
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        // If the word can be found starting from the current position, return true.
        if (dfs(board, i, j, word, 0)) return true;
      }
    }

    // If the word cannot be found in the board, return false.
    return false;
  }
}
