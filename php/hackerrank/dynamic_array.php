<?php

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    function dynamicArray($n, $queries)
    {
        $lastAnswer = 0;
        $seqList = [];
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $seqList[] = [];
        }
        foreach ($queries as $query) {
            $type = $query[0];
            $x = $query[1];
            $y = $query[2];
            $index = ($x ^ $lastAnswer) % $n;
            if ($type == 1) {
                $seqList[$index][] = $y;
            } else {
                $size = count($seqList[$index]);
                $lastAnswer = $seqList[$index][$y % $size];
                $result[] = $lastAnswer;
            }
        }
        return $result;
    }

    $fptr = fopen(getenv("OUTPUT_PATH"), "w");

    $first_multiple_input = explode(' ', rtrim(fgets(STDIN)));

    $n = intval($first_multiple_input[0]);

    $q = intval($first_multiple_input[1]);

    $queries = array();

    for ($i = 0; $i < $q; $i++) {
        $queries_temp = rtrim(fgets(STDIN));

        $queries[] = array_map('intval', preg_split('/ /', $queries_temp, -1, PREG_SPLIT_NO_EMPTY));
    }

    $result = dynamicArray($n, $queries);

    fwrite($fptr, implode("\n", $result) . "\n");

    fclose($fptr);
