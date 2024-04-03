func maxSubarrayLength(nums []int, k int) int {
	left := 0
	counter := make(map[int]int)
	maxLength := 0
	for right, num := range nums {
		counter[num]++
		for counter[num] > k {
			counter[nums[left]]--
			if counter[nums[left]] == 0 {
				delete(counter, nums[left])
			}
			left++
		}
		if right-left+1 > maxLength {
			maxLength = right - left + 1
		}
	}
	return maxLength
}
