<?php

class Solution
{

    /**
     * @param String $s
     * @return Boolean
     */
    function checkValidString(string $s): bool
    {
        $low = 0;
        $high = 0;
        for ($i = 0, $iMax = strlen($s); $i < $iMax; $i++) {
            if ($s[$i] === '(') {
                $low++;
                $high++;
            } else if ($s[$i] === ')') {
                $low--;
                $high--;
            } else {
                $low--;
                $high++;
            }
            if ($high < 0) {
                return false;
            }
            $low = max($low, 0);
        }
        return $low === 0;
    }
}
