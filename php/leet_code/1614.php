<?php

    class Solution
    {

        /**
         * @param String $s
         * @return Integer
         */
        function maxDepth($s)
        {
            $max = 0;
            $depth = 0;
            for ($i = 0, $iMax = strlen($s); $i < $iMax; $i++) {
                if ($s[$i] === '(') {
                    $depth++;
                    $max = max($max, $depth);
                } elseif ($s[$i] === ')') {
                    $depth--;
                }
            }
            return $max;
        }
    }