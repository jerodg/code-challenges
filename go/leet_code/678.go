package leet_code

func checkValidString(s string) bool {
	left, right := 0, 0
	for _, c := range s {
		if c == '(' {
			left++
		} else {
			left--
		}
		if c != ')' {
			right++
		} else {
			right--
		}
		if right < 0 {
			break
		}
		left = max(left, 0)
	}
	return left == 0
}
