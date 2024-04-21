<?php

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function hourglassSum($arr)
{
    $maxSum = PHP_INT_MIN;
    for ($i = 1; $i < 5; $i++) {
        for ($j = 1; $j < 5; $j++) {
            $top = $arr[$i - 1][$j - 1] + $arr[$i - 1][$j] + $arr[$i - 1][$j + 1];
            $mid = $arr[$i][$j];
            $bottom = $arr[$i + 1][$j - 1] + $arr[$i + 1][$j] + $arr[$i + 1][$j + 1];
            $hourglassSum = $top + $mid + $bottom;
            $maxSum = max($maxSum, $hourglassSum);
        }
    }
    return $maxSum;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$arr = array();

for ($i = 0; $i < 6; $i++) {
    $arr_temp = rtrim(fgets(STDIN));

    $arr[] = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));
}

$result = hourglassSum($arr);

fwrite($fptr, $result . "\n");

fclose($fptr);
