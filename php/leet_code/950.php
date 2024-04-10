<?php

    class Solution
    {

        /**
         * @param Integer[] $deck
         * @return Integer[]
         */
        function deckRevealedIncreasing($deck)
        {
            $n = count($deck);
            sort($deck);
            $q = new SplQueue();
            $ans = array_fill(0, $n, 0);
            for ($i = 0; $i < $n; $i++) {
                $q->enqueue($i);
            }
            for ($i = 0; $i < $n; $i++) {
                $idx = $q->dequeue();
                $ans[$idx] = $deck[$i];
                if (!$q->isEmpty()) {
                    $q->enqueue($q->dequeue());
                }
            }
            return $ans;
        }
    }
