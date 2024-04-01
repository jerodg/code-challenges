package leet_code

func merge(nums1 []int, m int, nums2 []int, n int) {
	for i := m + n - 1; i >= 0; i-- {
		if m == 0 {
			nums1[i] = nums2[n-1]
			n--
			continue
		}

		if n == 0 {
			return
		}

		if nums1[m-1] > nums2[n-1] {
			nums1[i] = nums1[m-1]
			m--
		} else {
			nums1[i] = nums2[n-1]
			n--
		}
	}
}
