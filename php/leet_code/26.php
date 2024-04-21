<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums)
    {
        $i = 0;
        $j = 1;
        $len = count($nums);
        while ($j < $len) {
            if ($nums[$i] != $nums[$j]) {
                $i++;
                $nums[$i] = $nums[$j];
            }
            $j++;
        }
        return $i + 1;
    }
}
