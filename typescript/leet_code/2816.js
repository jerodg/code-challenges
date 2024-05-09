/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */
/**
 * ListNode is a class that represents a node in a singly linked list.
 * Each node has a value and a reference to the next node in the list.
 */
var ListNode = /** @class */ (function () {
    /**
     * Constructs a new ListNode.
     * @param val - The value of the node. Defaults to 0 if not provided.
     * @param next - The next node in the list. Defaults to null if not provided.
     */
    function ListNode(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
    return ListNode;
}());
/**
 * Doubles the value of each node in the linked list.
 * If the doubled value is greater than 9, only the last digit is kept and 1 is carried over to the next node.
 * @param head - The head of the linked list.
 * @returns The head of the modified linked list.
 */
function doubleIt(head) {
    var rem = 0; // The carryover from the previous node.
    /**
     * A helper function that recursively visits each node in the list from last to first.
     * @param node - The current node.
     */
    var f = function (node) {
        if (!node) {
            return;
        }
        f(node.next);
        var doubled = node.val * 2 + rem; // Double the value of the node and add the carryover.
        rem = 0; // Reset the carryover.
        // If the doubled value is greater than 9, keep only the last digit and carry over 1 to the next node.
        if (doubled > 9) {
            doubled %= 10;
            rem = 1;
        }
        node.val = doubled; // Update the value of the node.
    };
    f(head);
    // If there is a carryover after visiting all nodes, add a new node at the beginning of the list.
    return rem ? new ListNode(1, head) : head;
}
