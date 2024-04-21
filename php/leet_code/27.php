<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val)
    {
        $i = 0;
        $n = count($nums);
        for ($j = 0; $j < $n; $j++) {
            if ($nums[$j] != $val) {
                $nums[$i] = $nums[$j];
                $i++;
            }
        }
        return $i;
    }
}
