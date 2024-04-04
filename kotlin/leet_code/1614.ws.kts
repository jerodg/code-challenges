class Solution {
    fun maxDepth(s: String): Int {
        var max = 0
        var count = 0
        for (c in s) {
            if (c == '(') {
                count++
                max = maxOf(max, count)
            } else if (c == ')') {
                count--
            }
        }
        return max
    }
}