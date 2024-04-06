<?php

    class Solution
    {

        /**
         * @param String $s
         * @return String
         */
        function minRemoveToMakeValid($s)
        {
            $stack = [];
            $s = str_split($s);
            foreach ($s as $i => $iValue) {
                if ($iValue === '(') {
                    $stack[] = $i;
                } else if ($iValue === ')') {
                    if (count($stack) > 0) {
                        array_pop($stack);
                    } else {
                        $s[$i] = '';
                    }
                }
            }
            foreach ($stack as $i) {
                $s[$i] = '';
            }
            return implode('', $s);
        }
    }