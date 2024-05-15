// Copyright © 2010-2024 JerodG <https://github.com/jerodg/>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

// Package leet_code provides solutions for LeetCode problems.
package leet_code

import (
	"container/heap"
	"math"
)

// Item represents a point in the grid with its distance from the nearest obstacle.
type Item struct {
	i, j, dist int // i and j are the coordinates of the point, dist is the distance from the nearest obstacle.
}

// PriorityQueue is a priority queue where items with larger distances have higher priority.
type PriorityQueue struct {
	items []Item // items is a slice of Item that forms the priority queue.
}

// Less returns true if the item at index i has higher priority than the item at index j.
func (pq *PriorityQueue) Less(i, j int) bool {
	return pq.items[i].dist > pq.items[j].dist
}

// Len returns the number of items in the priority queue.
func (pq *PriorityQueue) Len() int {
	return len(pq.items)
}

// Swap swaps the items at index i and j in the priority queue.
func (pq *PriorityQueue) Swap(i, j int) {
	pq.items[i], pq.items[j] = pq.items[j], pq.items[i]
}

// Push adds an item to the priority queue.
func (pq *PriorityQueue) Push(t interface{}) {
	pq.items = append(pq.items, t.(Item))
}

// Pop removes and returns the highest priority item from the priority queue.
func (pq *PriorityQueue) Pop() interface{} {
	n := len(pq.items)
	ret := pq.items[n-1]
	pq.items = pq.items[0 : n-1]
	return ret
}

// queue is a simple queue of Items.
type queue struct {
	items []Item // items is a slice of Item that forms the queue.
}

// Push adds an item to the end of the queue.
func (q *queue) Push(t Item) {
	q.items = append(q.items, t)
}

// Pop removes and returns the item at the front of the queue.
func (q *queue) Pop() Item {
	ret := q.items[0]
	q.items = q.items[1:]
	return ret
}

// IsEmpty returns true if the queue is empty.
func (q *queue) IsEmpty() bool {
	return len(q.items) == 0
}

// maximumSafenessFactor calculates the maximum safeness factor for a path from the top-left to the bottom-right of the grid.
// The safeness factor of a path is the minimum distance to an obstacle along the path.
// The function returns 0 if there is no such path.
func maximumSafenessFactor(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	if grid[0][0] == 1 || grid[m-1][n-1] == 1 {
		return 0
	}

	distance := generateDist(grid)
	pq := &PriorityQueue{}
	cost := make([][]int, m*n)
	for i := 0; i < m; i++ {
		cost[i] = make([]int, n)
		for j := 0; j < n; j++ {
			cost[i][j] = 0
		}
	}
	cost[0][0] = distance[0][0]
	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	heap.Push(pq, Item{0, 0, distance[0][0]})
	for pq.Len() > 0 {
		item := heap.Pop(pq).(Item)
		i, j, dist := item.i, item.j, item.dist
		if i == m-1 && j == n-1 {
			return dist
		}
		for _, dir := range directions {
			ni, nj := i+dir[0], j+dir[1]
			if ni < 0 || ni >= m || nj < 0 || nj >= n {
				continue
			}
			newDist := min(dist, distance[ni][nj])
			if newDist > cost[ni][nj] {
				cost[ni][nj] = newDist
				heap.Push(pq, Item{ni, nj, newDist})
			}
		}
	}
	return 0
}

// generateDist generates a 2D grid of distances to the nearest obstacle for each point in the input grid.
// The function uses Breadth-First Search (BFS) to calculate the distances.
func generateDist(grid [][]int) [][]int {
	m, n := len(grid), len(grid[0])
	distance := make([][]int, m*n)
	for i := 0; i < m; i++ {
		distance[i] = make([]int, n)
		for j := 0; j < n; j++ {
			distance[i][j] = math.MaxInt32
		}
	}

	queue := &queue{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				distance[i][j] = 0
				queue.Push(Item{i, j, 0})
			}
		}
	}

	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for !queue.IsEmpty() {
		item := queue.Pop()
		i, j, dist := item.i, item.j, item.dist
		for _, dir := range directions {
			ni, nj := i+dir[0], j+dir[1]
			if ni < 0 || ni >= m || nj < 0 || nj >= n || distance[ni][nj] != math.MaxInt32 {
				continue
			}
			distance[ni][nj] = dist + 1
			queue.Push(Item{ni, nj, dist + 1})
		}
	}
	return distance
}
