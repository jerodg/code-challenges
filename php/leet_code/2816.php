<?php
declare(strict_types=1);

/**
 * Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Server Side Public License (SSPL) as
 * published by MongoDB, Inc., either version 1 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * You should have received a copy of the SSPL along with this program.
 * If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * Class ListNode
 *
 * This class represents a node in a singly linked list. Each node contains a value and a reference to the next node.
 */
class ListNode
{
    /**
     * @var mixed The value stored in the node.
     */
    public mixed $val = 0;

    /**
     * @var ListNode|null The next node in the linked list.
     */
    public ?ListNode $next = null;

    /**
     * ListNode constructor.
     *
     * @param int|null $val The value to be stored in the node.
     * @param ListNode|null $next The next node in the linked list.
     */
    public function __construct(null|int $val = 0, ListNode $next = null)
    {
        $this->val = $val;
        $this->next = $next;
    }
}

/**
 * Class Solution
 *
 * This class provides a solution for doubling the value of each node in a linked list.
 */
class Solution
{
    /**
     * Doubles the value of each node in a linked list.
     *
     * The function iterates through the linked list, doubling the value of each node.
     * If the value of a node is greater than or equal to 5, a new node with a value of 0 is added before it.
     *
     * @param ListNode $head The head of the linked list.
     * @return ListNode The head of the modified linked list.
     */
    public function doubleIt(ListNode $head): ListNode
    {
        if ($head->val >= 5) {
            $head = new ListNode(0, $head);
        }
        $current = $head;
        while ($current->next) {
            $current->val = ($current->val * 2) % 10;
            if ($current->next->val >= 5) {
                $current->val++;
            }
            $current = $current->next;
        }
        $current->val = ($current->val * 2) % 10; // Handle the last node
        return $head;
    }
}
