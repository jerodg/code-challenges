<?php

class Solution
{
    public function wordBreak($s, $wordDict): array
    {
        $set = array_flip($wordDict);
        $dp = array_fill(0, strlen($s) + 1, false);
        $dp[0] = true;
        for ($i = 1, $iMax = strlen($s); $i <= $iMax; $i++) {
            for ($j = 0; $j < $i; $j++) {
                if ($dp[$j] && isset($set[substr($s, $j, $i - $j)])) {
                    $dp[$i] = true;
                    break;
                }
            }
        }
        $result = [];
        if ($dp[strlen($s)]) {
            $this->dfs($s, $set, $dp, 0, '', $result);
        }
        return $result;
    }

    public function dfs($s, $set, $dp, $start, $current, &$result): void
    {
        if ($start == strlen($s)) {
            $result[] = trim($current);
        } else {
            for ($i = $start + 1, $iMax = strlen($s); $i <= $iMax; $i++) {
                $substr = substr($s, $start, $i - $start);
                if ($dp[$i] && isset($set[$substr])) {
                    $this->dfs($s, $set, $dp, $i, $current . $substr . ' ', $result);
                }
            }
        }
    }
}
