package leet_code

func removeElement(nums []int, val int) int {
	var i int
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i++
		}
	}
	return i
}