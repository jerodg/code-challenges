# @param {Character[][]} board
# @param {String} word
# @return {Boolean}

# fixme: Not completing in the allowed time; need to optimize.
def exist(board, word)
  return false if board.empty? || board[0].empty? || word.empty?

  @word = word
  @board = board
  @row = board.length
  @col = board[0].length
  @directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

  # Check if the word contains any characters not present in the board
  char_freq = Hash.new(0)
  board.each { |row| row.each { |c| char_freq[c] += 1 if ('a'..'z').include?(c) } }
  return false if word.chars.any? { |c| char_freq[c].zero? }

  first_char = word[0]
  starting_positions = []
  @row.times do |r|
    @col.times do |c|
      starting_positions << [r, c] if @board[r][c] == first_char
    end
  end

  starting_positions.each do |r, c|
    visited = Set.new
    if dfs(r, c, 0, visited)
      return true
    end
  end

  false
end

def dfs(r, c, index, visited)
  return false if r < 0 || r >= @row || c < 0 || c >= @col || visited.include?([r, c]) || @board[r][c] != @word[index]
  return true if index == @word.length - 1

  visited.add([r, c])
  @directions.each do |d|
    if dfs(r + d[0], c + d[1], index + 1, visited)
      return true
    end
  end
  visited.delete([r, c])
  false
end