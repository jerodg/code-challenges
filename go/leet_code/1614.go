package leet_code

func maxDepth(s string) int {
	var max, count int
	for _, c := range s {
		if c == '(' {
			count++
			if count > max {
				max = count
			}
		} else if c == ')' {
			count--
		}
	}
	return max
}