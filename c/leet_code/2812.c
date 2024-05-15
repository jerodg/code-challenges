/**
 * @file leet_code/2812.c
 * @brief This file contains the implementation of a MaxHeap and various functions to solve a problem related to a grid.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */
#pragma GCC optimize("O3,unroll-loops")

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * @brief A structure to represent a Node in the heap.
 *
 * @param dist The distance of the node.
 * @param i The row index of the node in the grid.
 * @param j The column index of the node in the grid.
 */
typedef struct {
    int dist;
    int i;
    int j;
} Node;

/**
 * @brief A structure to represent a MaxHeap.
 *
 * @param data The array of Nodes in the heap.
 * @param size The current size of the heap.
 * @param capacity The total capacity of the heap.
 */
typedef struct {
    Node* data;
    int size;
    int capacity;
} maxHeap;

/**
 * @brief Initializes a MaxHeap with a given capacity.
 *
 * @param heap The MaxHeap to be initialized.
 * @param capacity The initial capacity of the heap.
 */
void maxHeapInit(maxHeap* heap, int capacity) {
    heap->data = (Node*)malloc(sizeof(Node) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
}

/**
 * @brief Pushes a Node into the MaxHeap.
 *
 * @param heap The MaxHeap to push the Node into.
 * @param node The Node to be pushed.
 */
void maxHeapPush(maxHeap* heap, Node node) {
    if (heap->size == heap->capacity) {
        heap->capacity *= 2;
        heap->data = (Node*)realloc(heap->data, sizeof(Node) * heap->capacity);
    }
    heap->data[heap->size] = node;
    int current = heap->size;
    heap->size++;
    while (current > 0) {
        int parent = (current - 1) / 2;
        if (heap->data[current].dist > heap->data[parent].dist) {
            Node temp = heap->data[current];
            heap->data[current] = heap->data[parent];
            heap->data[parent] = temp;
            current = parent;
        } else {
            break;
        }
    }
}

/**
 * @brief Pops the top Node from the MaxHeap.
 *
 * @param heap The MaxHeap to pop the Node from.
 * @return Node The popped Node.
 */
Node maxHeapPop(maxHeap* heap) {
    Node top = heap->data[0];
    heap->size--;
    heap->data[0] = heap->data[heap->size];
    int current = 0;
    while (true) {
        int leftChild = 2 * current + 1;
        int rightChild = 2 * current + 2;
        int largest = current;
        if (leftChild < heap->size && heap->data[leftChild].dist > heap->data[largest].dist) {
            largest = leftChild;
        }
        if (rightChild < heap->size && heap->data[rightChild].dist > heap->data[largest].dist) {
            largest = rightChild;
        }
        if (largest != current) {
            Node temp = heap->data[current];
            heap->data[current] = heap->data[largest];
            heap->data[largest] = temp;
            current = largest;
        } else {
            break;
        }
    }
    return top;
}

/**
 * @brief Checks if a given position is valid in the grid.
 *
 * @param x The row index of the position.
 * @param y The column index of the position.
 * @param n The size of the grid.
 * @return bool True if the position is valid, false otherwise.
 */
bool isValid(int x, int y, int n) { return x >= 0 && x < n && y >= 0 && y < n; }

/**
 * @brief Computes a distance grid from the given grid.
 *
 * @param grid The given grid.
 * @param gridSize The size of the grid.
 * @return int** The computed distance grid.
 */
int** computeDistanceGrid(int** grid, int gridSize) {
    int n = gridSize;
    int** distGrid = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        distGrid[i] = (int*)malloc(n * sizeof(int));
        for (int j = 0; j < n; j++) {
            distGrid[i][j] = INT_MAX;
        }
    }

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int queue[n * n][2];
    int front = 0, rear = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                queue[rear][0] = i;
                queue[rear][1] = j;
                rear++;
                distGrid[i][j] = 0;
            }
        }
    }

    while (front < rear) {
        int x = queue[front][0];
        int y = queue[front][1];
        front++;
        for (int d = 0; d < 4; d++) {
            int newX = x + directions[d][0];
            int newY = y + directions[d][1];
            if (isValid(newX, newY, n) && distGrid[newX][newY] == INT_MAX) {
                distGrid[newX][newY] = distGrid[x][y] + 1;
                queue[rear][0] = newX;
                queue[rear][1] = newY;
                rear++;
            }
        }
    }

    return distGrid;
}

/**
 * @brief Computes the maximum safeness factor of the given grid.
 *
 * @param grid The given grid.
 * @param gridSize The size of the grid.
 * @param gridColSize The size of the columns in the grid.
 * @return int The maximum safeness factor.
 */
int maximumSafenessFactor(int** grid, int gridSize, __attribute__((unused)) int* gridColSize) {
    int n = gridSize;
    if (grid[n - 1][n - 1] == 1 || grid[0][0] == 1) {
        return 0;
    }

    int** dist = computeDistanceGrid(grid, n);
    maxHeap heap;
    maxHeapInit(&heap, n * n);
    bool** vis = (bool**)malloc(n * sizeof(bool*));
    for (int i = 0; i < n; i++) {
        vis[i] = (bool*)calloc(n, sizeof(bool));
    }

    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    maxHeapPush(&heap, (Node){dist[0][0], 0, 0});
    vis[0][0] = true;

    while (heap.size > 0) {
        Node node = maxHeapPop(&heap);
        int ds = node.dist, i = node.i, j = node.j;

        if (i == n - 1 && j == n - 1) {
            free(dist);
            for (int k = 0; k < n; k++) {
                free(vis[k]);
            }
            free(vis);
            free(heap.data);
            return ds;
        }

        for (int d = 0; d < 4; d++) {
            int newRow = i + directions[d][0];
            int newCol = j + directions[d][1];
            if (isValid(newRow, newCol, n) && grid[newRow][newCol] != 1 && !vis[newRow][newCol]) {
                vis[newRow][newCol] = true;
                int ds1 = dist[newRow][newCol];
                maxHeapPush(&heap, (Node){ds < ds1 ? ds : ds1, newRow, newCol});
            }
        }
    }

    free(dist);
    for (int k = 0; k < n; k++) {
        free(vis[k]);
    }
    free(vis);
    free(heap.data);

    return 0;
}
