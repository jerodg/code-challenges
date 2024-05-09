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
 * MaxHeap is a generic class that implements a max heap data structure.
 * A max heap is a specialized tree-based data structure that satisfies the heap property.
 * In a max heap, for any given node I, the value of I is greater than the values of its children.
 */
var MaxHeap = /** @class */ (function () {
    function MaxHeap() {
        this.heap = [];
    }
    /**
     * Returns the index of the parent of the node at index i.
     * @param i - The index of the node.
     * @returns The index of the parent.
     */
    MaxHeap.prototype.getParentIndex = function (i) {
        return Math.floor((i - 1) / 2);
    };
    /**
     * Returns the index of the left child of the node at index i.
     * @param i - The index of the node.
     * @returns The index of the left child.
     */
    MaxHeap.prototype.getLeftChildIndex = function (i) {
        return 2 * i + 1;
    };
    /**
     * Returns the index of the right child of the node at index i.
     * @param i - The index of the node.
     * @returns The index of the right child.
     */
    MaxHeap.prototype.getRightChildIndex = function (i) {
        return 2 * i + 2;
    };
    /**
     * Checks if the node at index i has a parent.
     * @param i - The index of the node.
     * @returns True if the node has a parent, false otherwise.
     */
    MaxHeap.prototype.hasParent = function (i) {
        return this.getParentIndex(i) >= 0;
    };
    /**
     * Checks if the node at index i has a left child.
     * @param i - The index of the node.
     * @returns True if the node has a left child, false otherwise.
     */
    MaxHeap.prototype.hasLeftChild = function (i) {
        return this.getLeftChildIndex(i) < this.heap.length;
    };
    /**
     * Checks if the node at index i has a right child.
     * @param i - The index of the node.
     * @returns True if the node has a right child, false otherwise.
     */
    MaxHeap.prototype.hasRightChild = function (i) {
        return this.getRightChildIndex(i) < this.heap.length;
    };
    /**
     * Swaps the elements at the given indices in the heap.
     * @param i - The first index.
     * @param j - The second index.
     */
    MaxHeap.prototype.swap = function (i, j) {
        var temp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = temp;
    };
    /**
     * Checks if the heap is empty.
     * @returns True if the heap is empty, false otherwise.
     */
    MaxHeap.prototype.isEmpty = function () {
        return this.heap.length === 0;
    };
    /**
     * Inserts an item into the heap.
     * @param item - The item to be inserted.
     */
    MaxHeap.prototype.insert = function (item) {
        this.heap.push(item);
        this.siftUp(this.heap.length - 1);
    };
    /**
     * Sifts up the element at the given index, ensuring the heap property is maintained.
     * @param i - The index of the element to sift up.
     */
    MaxHeap.prototype.siftUp = function (i) {
        while (this.hasParent(i) && this.heap[i] > this.heap[this.getParentIndex(i)]) {
            this.swap(i, this.getParentIndex(i));
            i = this.getParentIndex(i);
        }
    };
    /**
     * Extracts (removes and returns) the maximum element from the heap.
     * @returns The maximum element, or undefined if the heap is empty.
     */
    MaxHeap.prototype.extractMax = function () {
        if (this.isEmpty()) {
            return undefined;
        }
        var root = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.siftDown(0);
        return root;
    };
    /**
     * Sifts down the element at the given index, ensuring the heap property is maintained.
     * @param i - The index of the element to sift down.
     */
    MaxHeap.prototype.siftDown = function (i) {
        while (this.hasLeftChild(i) &&
            (this.heap[i] < this.heap[this.getLeftChildIndex(i)] ||
                (this.hasRightChild(i) && this.heap[i] < this.heap[this.getRightChildIndex(i)]))) {
            var largerChildIndex = this.hasRightChild(i) && this.heap[this.getLeftChildIndex(i)] < this.heap[this.getRightChildIndex(i)]
                ? this.getRightChildIndex(i)
                : this.getLeftChildIndex(i);
            this.swap(i, largerChildIndex);
            i = largerChildIndex;
        }
    };
    return MaxHeap;
}());
/**
 * Calculates the maximum sum of happiness that can be achieved by attending k parties.
 * @param happiness - An array where each element represents the happiness gained from attending a party.
 * @param k - The number of parties that can be attended.
 * @returns The maximum sum of happiness.
 */
function maximumHappinessSum(happiness, k) {
    var i = 0;
    var heap = new MaxHeap();
    for (var i_1 = 0; i_1 < happiness.length; i_1++) {
        heap.insert(happiness[i_1]);
    }
    var res = 0;
    while (!heap.isEmpty() && k > 0) {
        var top_1 = heap.extractMax() || 0;
        res += Math.max(top_1 - i, 0);
        i++;
        k--;
    }
    return res;
}
