<?php

class Solution
{

    /**
     * @param Integer[] $students
     * @param Integer[] $sandwiches
     * @return Integer
     */
    public function countStudents(array $students, array $sandwiches): int
    {
        $queue = new SplQueue();
        foreach ($students as $student) {
            $queue->enqueue($student);
        }

        $stack = new SplStack();
        for ($i = count($sandwiches) - 1; $i >= 0; $i--) {
            $stack->push($sandwiches[$i]);
        }

        $count = 0;
        while (!$queue->isEmpty() && $count < count($students)) {
            $student = $queue->dequeue();
            if ($student == $stack->top()) {
                $stack->pop();
                $count = 0;
            } else {
                $queue->enqueue($student);
                $count++;
            }
        }

        return $queue->count();
    }
}
