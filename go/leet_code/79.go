package leet_code

func dfs(board [][]byte, i, j int, word string, k int) bool {
	if i < 0 || i >= len(board) || j < 0 || j >= len(board[i]) {
		return false
	}

	if board[i][j] != word[k] {
		return false
	}

	if k == len(word)-1 {
		return true
	}

	tmp := board[i][j]
	board[i][j] = '.'

	if dfs(board, i-1, j, word, k+1) || dfs(board, i+1, j, word, k+1) || dfs(board, i, j-1, word, k+1) || dfs(board, i, j+1, word, k+1) {
		return true
	}

	board[i][j] = tmp

	return false
}

func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if dfs(board, i, j, word, 0) {
				return true
			}
		}
	}

	return false
}
