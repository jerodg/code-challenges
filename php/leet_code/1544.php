<?php

class Solution
{

    /**
     * @param String $s
     * @return String
     */
    public function makeGood($s)
    {
        $stack = [];
        for ($i = 0, $iMax = strlen($s); $i < $iMax; $i++) {
            $c = $s[$i];
            if (empty($stack)) {
                $stack[] = $c;
            } else {
                $top = end($stack);
                if (abs(ord($top) - ord($c)) === 32) {
                    array_pop($stack);
                } else {
                    $stack[] = $c;
                }
            }
        }
        return implode('', $stack);
    }
}
