<?php

class Solution
{

    public function exist($board, $word)
    {
        $word = str_split($word);
        $word_len = count($word);
        $board_row = count($board);
        $board_col = count($board[0]);
        $visited = [];
        for ($i = 0; $i < $board_row; $i++) {
            for ($j = 0; $j < $board_col; $j++) {
                if ($board[$i][$j] == $word[0]) {
                    $visited[$i][$j] = true;
                    if ($this->dfs($board, $word, 1, $i, $j, $visited)) {
                        return true;
                    }
                    $visited[$i][$j] = false;
                }
            }
        }
        return false;
    }

    /**
     * @param String[][] $board
     * @param String $word
     * @return Boolean
     */
    public function dfs($board, $word, $index, $i, $j, $visited)
    {
        if ($index == count($word)) {
            return true;
        }
        $directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        foreach ($directions as $direction) {
            $new_i = $i + $direction[0];
            $new_j = $j + $direction[1];
            if ($new_i >= 0 && $new_i < count($board) && $new_j >= 0 && $new_j < count($board[0]) && !$visited[$new_i][$new_j] && $board[$new_i][$new_j] == $word[$index]) {
                $visited[$new_i][$new_j] = true;
                if ($this->dfs($board, $word, $index + 1, $new_i, $new_j, $visited)) {
                    return true;
                }
                $visited[$new_i][$new_j] = false;
            }
        }
        return false;
    }
}
