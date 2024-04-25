package leet_code

func timeRequiredToBuy(tickets []int, k int) int {
	result := 0
	c := tickets[k]
	for i, n := range tickets {
		if i == k {
			result += c
		} else if i < k {
			result += minimum(c, n)
		} else {
			result += minimum(c-1, n)
		}
	}
	return result
}
