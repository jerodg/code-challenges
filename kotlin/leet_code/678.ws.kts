class Solution {
    fun checkValidString(s: String): Boolean {
        var low = 0
        var high = 0
        for (c in s) {
            low += if (c == '(') 1 else -1
            high += if (c != ')') 1 else -1
            if (high < 0) break
            low = maxOf(low, 0)
        }
        return low == 0
    }
}