impl Solution {
    pub fn dfs(board: &Vec<Vec<char>>, word: &String, index: usize, i: i32, j: i32) -> bool {
        if i < 0 || i >= board.len() as i32 || j < 0 || j >= board[0].len() as i32 || board[i as usize][j as usize] != word.chars().nth(index).unwrap() {
            return false;
        }
        if index == word.len() - 1 {
            return true;
        }
        let temp = board[i as usize][j as usize];
        let mut board = board.clone();
        board[i as usize][j as usize] = ' ';
        let res = Solution::dfs(&board, word, index + 1, i + 1, j)
            || Solution::dfs(&board, word, index + 1, i - 1, j)
            || Solution::dfs(&board, word, index + 1, i, j + 1)
            || Solution::dfs(&board, word, index + 1, i, j - 1);
        board[i as usize][j as usize] = temp;
        res
    }
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        for i in 0..board.len() {
            for j in 0..board[0].len() {
                if Solution::dfs(&board, &word, 0, i as i32, j as i32) {
                    return true;
                }
            }
        }
        false
    }
}
