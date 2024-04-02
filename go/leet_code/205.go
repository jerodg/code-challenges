package leet_code

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	m1 := make(map[byte]byte)
	m2 := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		if _, ok := m1[s[i]]; !ok {
			m1[s[i]] = t[i]
		} else if m1[s[i]] != t[i] {
			return false
		}

		if _, ok := m2[t[i]]; !ok {
			m2[t[i]] = s[i]
		} else if m2[t[i]] != s[i] {
			return false
		}
	}

	return true
}
