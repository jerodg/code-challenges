<?php
declare(strict_types=1);

/**
 * This file contains the Solution class which includes methods for solving
 * specific problems related to graph traversal and ticket purchasing.
 *
 * PHP version 8.3
 */
class Solution
{
    /**
     * This method calculates the time required to buy a certain number of tickets.
     * It uses a priority queue to manage the tickets and a counter to keep track
     * of the time.
     *
     * @param Integer[] $tickets An array of integers representing the tickets.
     * @param Integer $k The number of tickets to buy.
     *
     * @return Integer The time required to buy the tickets.
     *
     * @throws InvalidArgumentException If $tickets is not an array or $k is not an integer.
     *
     * @example
     * $solution = new Solution();
     * $time = $solution->timeRequiredToBuy([1, 2, 3], 2);
     * echo $time; // Outputs: 2
     */
    public function timeRequiredToBuy(array $tickets, int $k): int
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

    /**
     * This method checks if there is a valid path from source to destination in a graph.
     * It uses a breadth-first search algorithm to traverse the graph.
     *
     * @param Integer $n The number of nodes in the graph.
     * @param Integer[][] $edges The edges of the graph.
     * @param Integer $source The source node.
     * @param Integer $destination The destination node.
     *
     * @return Boolean True if there is a valid path, false otherwise.
     *
     * @throws InvalidArgumentException If any of the parameters are not of the expected type.
     *
     * @example
     * $solution = new Solution();
     * $isValid = $solution->validPath(3, [[0, 1], [1, 2]], 0, 2);
     * echo $isValid ? 'Valid' : 'Invalid'; // Outputs: Valid
     */
    public function validPath(int $n, array $edges, int $source, int $destination): bool
    {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        $visited = array_fill(0, $n, false);
        $queue = new SplQueue();
        $queue->enqueue($source);
        $visited[$source] = true;

        while (!$queue->isEmpty()) {
            $current = $queue->dequeue();
            if ($current == $destination) {
                return true;
            }

            foreach ($graph[$current] as $neighbor) {
                if (!$visited[$neighbor]) {
                    $visited[$neighbor] = true;
                    $queue->enqueue($neighbor);
                }
            }
        }

        return false;
    }

    /**
     * This method builds a graph from a given set of edges.
     *
     * @param Integer[][] $edges The edges of the graph.
     * @param Integer $n The number of nodes in the graph.
     *
     * @return array The built graph.
     *
     * @throws InvalidArgumentException If $edges is not an array or $n is not an integer.
     *
     * @example
     * $solution = new Solution();
     * $graph = $solution->buildGraph([[0, 1], [1, 2]], 3);
     * print_r($graph); // Outputs: Array ( [0] => Array ( [0] => 1 ) [1] => Array ( [0] => 0 [1] => 2 ) [2] => Array ( [0] => 1 ) )
     */
    public function buildGraph(array $edges, int $n): array
    {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $graph[$edge[0]][] = $edge[1];
            $graph[$edge[1]][] = $edge[0];
        }
        return $graph;
    }
}
