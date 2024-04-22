# Function to check if a word exists in a 2D board
#
# This function checks if a given word can be formed in the board by sequentially connecting cells horizontally or vertically.
# Each cell in the board contains a single letter, and the same letter cell may not be used more than once.
#
# @param board [Array<Array<String>>] The 2D board of letters
# @param word [String] The word to be checked
# @return [Boolean] True if the word exists in the board, false otherwise
#
# @example
#   exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED") #=> true
#
def exist(board, word)
  if word.match(/^#{word[0]}+/)[0].size > word.match(/#{word[-1]}+$/)[0].size
    word.reverse!
  end
  board.length.times do |i|
    board[0].length.times do |j|
      if board[i][j] == word[0]
        res = search(board, i, j, word)
        return true if res
      end
    end
  end
  false
end

# Function to search for a word in the board starting from a given cell
#
# @param board [Array<Array<String>>] The 2D board of letters
# @param i [Integer] The row index of the starting cell
# @param j [Integer] The column index of the starting cell
# @param word [String] The word to be searched
# @param idx [Integer] The index of the current character in the word
# @return [Boolean] True if the word is found, false otherwise
#
def search(board, i, j, word, idx = 0)
  if idx == word.length - 1 && board[i][j] == word[idx]
    true
  elsif board[i][j] != word[idx]
    return false
  else
    temp = board[i][j]
    board[i][j] = "*"
    [[-1, 0], [1, 0], [0, 1], [0, -1]].each do |off|
      ip, jp = i + off[0], j + off[1]
      if in_bounds?(ip, jp, board)
        res = search(board, ip, jp, word, idx + 1)
        return res if res
      end
    end
    board[i][j] = temp
    false
  end
end

# Function to check if a cell is within the bounds of the board
#
# @param i [Integer] The row index of the cell
# @param j [Integer] The column index of the cell
# @param board [Array<Array<String>>] The 2D board of letters
# @return [Boolean] True if the cell is within the bounds of the board, false otherwise
#
def in_bounds?(i, j, board)
  i >= 0 && j >= 0 && i < board.length && j < board[0].length
end