object Solution {
  def dfs(
      board: Array[Array[Char]],
      word: String,
      i: Int,
      j: Int,
      k: Int
  ): Boolean = {
    if (k == word.length) return true
    if (
      i < 0 || i >= board.length || j < 0 || j >= board(0).length || board(i)(
        j
      ) != word(k)
    ) return false
    val tmp = board(i)(j)
    board(i)(j) = ' '
    val res = dfs(board, word, i - 1, j, k + 1) || dfs(
      board,
      word,
      i + 1,
      j,
      k + 1
    ) || dfs(board, word, i, j - 1, k + 1) || dfs(board, word, i, j + 1, k + 1)
    board(i)(j) = tmp
    res
  }

  def exist(board: Array[Array[Char]], word: String): Boolean = {
    val m = board.length
    val n = board(0).length
    val visited = Array.fill(m, n)(false)
    def dfs(i: Int, j: Int, k: Int): Boolean = {
      if (k == word.length) return true
      if (
        i < 0 || i >= m || j < 0 || j >= n || visited(i)(j) || board(i)(
          j
        ) != word(k)
      ) return false
      visited(i)(j) = true
      val res = dfs(i - 1, j, k + 1) || dfs(i + 1, j, k + 1) || dfs(
        i,
        j - 1,
        k + 1
      ) || dfs(i, j + 1, k + 1)
      visited(i)(j) = false
      res
    }
    (0 until m).exists(i => (0 until n).exists(j => dfs(i, j, 0)))
  }
}
