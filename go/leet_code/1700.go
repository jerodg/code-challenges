package leet_code

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