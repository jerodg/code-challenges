# @param {Character[][]} board
# @param {String} word
# @return {Boolean}

def dfs(board, i, j, word)
  directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  stack = [[i, j, 0]]

  until stack.empty?
    x, y, index = stack.last
    if index < word.size && x >= 0 && x < board.size && y >= 0 && y < board[0].size && board[x][y] == word[index]
      return true if index == word.size - 1

      board[x][y] = "."
      index += 1
      directions.each { |dx, dy| stack.push([x + dx, y + dy, index]) }
    else
      x, y, _ = stack.pop
      board[x][y] = word[index - 1] if stack.empty? || stack.last[2] != index
    end
  end

  false
end

def exist(board, word)
  (0...board.length).each do |i|
    (0...board[0].length).each do |j|
      return true if dfs(board, i, j, word)
    end
  end
  false
end
