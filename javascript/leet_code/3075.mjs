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
 * This function calculates the maximum sum of happiness that can be achieved by selecting a certain number of children.
 * It uses a heap data structure to efficiently select the children with the highest happiness values.
 *
 * @param {number[]} happiness - An array of happiness values for each child. Each value is a positive integer.
 * @param {number} k - The number of children to select. This is a positive integer.
 * @returns {number} The maximum sum of happiness that can be achieved by selecting k children.
 */
const maximumHappinessSum = function (happiness, k) {
    // The number of children that have been selected so far
    let selected = 0;
    // A heap data structure that will be used to efficiently select the children with the highest happiness values
    let heap = new Heap((a, b) => a - b);
    // Insert each child's happiness value into the heap
    for (const child of happiness) {
        heap.insert(child);
    }
    // The current sum of happiness
    let result = 0;
    // While there are still children to select
    while (k - selected > 0) {
        // If the maximum happiness value in the heap minus the number of selected children is less than or equal to 0
        if (heap.peek() - selected <= 0) {
            // Return the current sum of happiness
            return result;
        } else {
            // Remove the maximum happiness value from the heap
            let val = heap.remove();
            // Subtract the number of selected children from the happiness value
            val -= selected;
            // Add the happiness value to the current sum of happiness
            result += val;
            // Increment the number of selected children
            selected++;
        }
    }
    // Return the maximum sum of happiness
    return result;
};

/**
 * This class represents a heap data structure. A heap is a complete binary tree that maintains the heap property:
 * for any given node i, the value of i is greater than or equal to the values of its children.
 *
 * @property {Array} heap - The underlying array representing the heap.
 * @property {function} comparator - The comparator function used to order the elements in the heap.
 */
class Heap {
    /**
     * Constructs a new Heap.
     *
     * @param {function} comparator - The comparator function used to order the elements in the heap.
     */
    constructor(comparator) {
        // The underlying array representing the heap
        this.heap = [];
        // The comparator function used to order the elements in the heap
        this.comparator = comparator;
    }

    /**
     * Inserts an element into the heap.
     *
     * @param {*} element - The element to insert.
     */
    insert(element) {
        // Add the element to the end of the heap
        this.heap.push(element);
        // Restore the heap property by moving the element up the heap
        this.heapifyUp();
    }

    /**
     * Removes and returns the maximum element from the heap.
     *
     * @returns {*} The maximum element from the heap.
     */
    remove() {
        // Store the maximum element
        const max = this.heap[0];
        // Replace the maximum element with the last element in the heap
        this.heap[0] = this.heap[this.heap.length - 1];
        // Remove the last element from the heap
        this.heap.pop();
        // Restore the heap property by moving the new maximum element down the heap
        this.heapifyDown();
        // Return the maximum element
        return max;
    }

    /**
     * Restores the heap property by moving the element at the specified index up the heap.
     */
    heapifyUp() {
        // Start at the last element in the heap
        let index = this.heap.length - 1;
        // While the element is not the root
        while (index > 0) {
            // Calculate the index of the parent element
            const parentIndex = Math.floor((index - 1) / 2);
            // If the element is greater than its parent
            if (this.comparator(this.heap[index], this.heap[parentIndex]) > 0) {
                // Swap the element with its parent
                this.swap(index, parentIndex);
                // Move to the parent element
                index = parentIndex;
            } else {
                // The element is not greater than its parent, so the heap property is restored
                break;
            }
        }
    }

    /**
     * Restores the heap property by moving the element at the specified index down the heap.
     */
    heapifyDown() {
        // Start at the root
        let index = 0;
        // While the element has at least one child
        while (index < this.heap.length) {
            // Calculate the indices of the child elements
            const leftChildIndex = 2 * index + 1;
            const rightChildIndex = 2 * index + 2;
            // Assume the element is the largest
            let largestChildIndex = index;
            // If the left child is larger than the element
            if (leftChildIndex < this.heap.length && this.comparator(this.heap[leftChildIndex],
                this.heap[largestChildIndex]) > 0) {
                // The left child is the largest
                largestChildIndex = leftChildIndex;
            }
            // If the right child is larger than the current largest
            if (rightChildIndex < this.heap.length && this.comparator(this.heap[rightChildIndex],
                this.heap[largestChildIndex]) > 0) {
                // The right child is the largest
                largestChildIndex = rightChildIndex;
            }
            // If the largest child is the element
            if (largestChildIndex === index) {
                // The heap property is restored
                break;
            } else {
                // Swap the element with the largest child
                this.swap(index, largestChildIndex);
                // Move to the largest child
                index = largestChildIndex;
            }
        }
    }

    /**
     * Swaps the elements at the specified indices in the heap.
     *
     * @param {number} index1 - The index of the first element.
     * @param {number} index2 - The index of the second element.
     */
    swap(index1, index2) {
        // Store the first element in a temporary variable
        const temp = this.heap[index1];
        // Replace the first element with the second element
        this.heap[index1] = this.heap[index2];
        // Replace the second element with the first element
        this.heap[index2] = temp;
    }

    /**
     * Returns the maximum element from the heap without removing it.
     *
     * @returns {*} The maximum element from the heap.
     */
    peek() {
        // Return the maximum element
        return this.heap[0];
    }
}
