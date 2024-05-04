// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of counting the number of students that cannot eat lunch.
// The students are in a queue and each student either prefers square sandwiches or circular sandwiches.
// The sandwiches are stacked and the student at the front of the queue takes the top sandwich if it is of the type they prefer, otherwise they go to the back of the queue.
// The process continues until no student can eat the top sandwich.
package leet_code

// countStudents counts the number of students that cannot eat lunch.
//
// It accepts two parameters:
// - students: a slice of integers where each integer is 0 if the student prefers square sandwiches and 1 if the student prefers circular sandwiches.
// - sandwiches: a slice of integers where each integer is 0 if the sandwich is square and 1 if the sandwich is circular.
//
// The function returns an integer representing the number of students that cannot eat lunch.
//
// The function uses a counter to keep track of the number of students that prefer each type of sandwich.
// It iterates over the sandwiches, and for each sandwich, if there is a student that prefers the type of the sandwich, it decrements the counter of that type, otherwise it breaks the loop.
//
// Time complexity analysis:
// - Best-case: O(n), when all students prefer the type of the top sandwich.
// - Worst-case: O(n), when all students prefer a type of sandwich that is not at the top.
// - Average-case: O(n), as we always have to iterate over each sandwich in the worst case.
func countStudents(students []int, sandwiches []int) int {
	var stuCount = make([]int, 2)
	for _, stu := range students {
		stuCount[stu]++
	}

	for _, sandwich := range sandwiches {
		if stuCount[sandwich] == 0 {
			break
		}
		stuCount[sandwich]--
	}

	return stuCount[0] + stuCount[1]
}
