<?php

    class Solution
    {

        /**
         * @param String $s
         * @param String $t
         * @return Boolean
         */
        function isIsomorphic($s, $t)
        {
            $s = str_split($s);
            $t = str_split($t);
            $s_map = [];
            $t_map = [];
            $s_len = count($s);
            $t_len = count($t);
            if ($s_len != $t_len) {
                return false;
            }
            for ($i = 0; $i < $s_len; $i++) {
                if (!isset($s_map[$s[$i]])) {
                    $s_map[$s[$i]] = $t[$i];
                } else {
                    if ($s_map[$s[$i]] != $t[$i]) {
                        return false;
                    }
                }
                if (!isset($t_map[$t[$i]])) {
                    $t_map[$t[$i]] = $s[$i];
                } else {
                    if ($t_map[$t[$i]] != $s[$i]) {
                        return false;
                    }
                }
            }
            return true;
        }
    }