class Solution:
    def dfs(self, board: list[list[str]], i: int, j: int, word: str, index: int) -> bool:
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
        board[i][j] = "."

        # Check if the word exists in the board
        if (self.dfs(board, i + 1, j, word, index + 1) or self.dfs(board, i - 1, j, word, index + 1) or self.dfs(board, i, j + 1,
                                                                                                                 word,
                                                                                                                 index + 1) or
                self.dfs(
                board, i, j - 1, word, index + 1)):
            return True

        # Restore the character in the board
        board[i][j] = temp

        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        # Iterate over the rows in the board
        for i in range(len(board)):
            # Iterate over the columns in the board
            for j in range(len(board[0])):
                # If the character in the board is the same as the first character
                # in the word, then check if the word exists in the board
                if board[i][j] == word[0] and self.dfs(board, i, j, word, 0):
                    return True
        return False
