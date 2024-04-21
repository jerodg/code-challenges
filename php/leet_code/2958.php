<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxSubarrayLength($nums, $k)
    {
        $left = 0;
        $counter = array();
        $maxLength = 0;
        foreach ($nums as $right => $num) {
            if (!array_key_exists($num, $counter)) {
                $counter[$num] = 0;
            }
            $counter[$num] += 1;
            while ($counter[$num] > $k) {
                $counter[$nums[$left]] -= 1;
                if ($counter[$nums[$left]] == 0) {
                    unset($counter[$nums[$left]]);
                }
                $left += 1;
            }
            $maxLength = max($maxLength, $right - $left + 1);
        }

        return $maxLength;
    }
}
