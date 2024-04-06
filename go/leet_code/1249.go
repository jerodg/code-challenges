package leet_code

func minRemoveToMakeValid(s string) string {
	var stack []int
	var remove []int
	for i, v := range s {
		if v == '(' {
			stack = append(stack, i)
		} else if v == ')' {
			if len(stack) == 0 {
				remove = append(remove, i)
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}
	remove = append(remove, stack...)
	var res []byte
	for i, v := range s {
		if len(remove) > 0 && i == remove[0] {
			remove = remove[1:]
			continue
		}
		res = append(res, byte(v))
	}
	return string(res)
}
