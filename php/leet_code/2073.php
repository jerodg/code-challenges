<?php

class Solution
{
    /**
     * @param Integer[] $tickets
     * @param Integer $k
     * @return Integer
     */
    function timeRequiredToBuy($tickets, $k)
    {
        $queue = new SplPriorityQueue();
        foreach ($tickets as $ticket) {
            $queue->insert($ticket, -$ticket); // negative value to sort in ascending order
        }

        $count = 0;
        while (!$queue->isEmpty()) {
            $ticket = $queue->extract();
            if ($ticket <= $k) {
                $k -= $ticket;
                $count++;
            } else {
                $queue->insert($ticket - $k, -($ticket - $k));
                $count++;
                $k = 0;
            }
        }
        return $count;
    }
}
// fixme: this exceeds the time limit
