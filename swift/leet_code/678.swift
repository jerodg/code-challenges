class Solution {
    func checkValidString(_ s: String) -> Bool {
        var left = 0
        var right = 0
        for c in s {
            if c == "(" || c == "*" {
                left += 1
            } else {
                left -= 1
            }
            if left < 0 {
                return false
            }
        }
        if left == 0 {
            return true
        }
        for c in s.reversed() {
            if c == ")" || c == "*" {
                right += 1
            } else {
                right -= 1
            }
            if right < 0 {
                return false
            }
        }
        return true
    }
}
