class Solution {
    fun makeGood(s: String): String {
        val stack = mutableListOf<Char>()
        for (c in s) {
            if (stack.isNotEmpty() && stack.last().toLowerCase() == c.toLowerCase() && stack.last() != c) {
                stack.removeAt(stack.size - 1)
            } else {
                stack.add(c)
            }
        }
        return stack.joinToString("")
    }
}