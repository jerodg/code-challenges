class Solution {
    fun minRemoveToMakeValid(s: String): String {
        val stack = mutableListOf<Int>()
        val sb = StringBuilder(s)
        for (i in s.indices) {
            if (s[i] == '(') {
                stack.add(i)
            } else if (s[i] == ')') {
                if (stack.isNotEmpty()) {
                    stack.removeAt(stack.size - 1)
                } else {
                    sb.setCharAt(i, ' ')
                }
            }
        }
        for (i in stack) {
            sb.setCharAt(i, ' ')
        }
        return sb.toString().replace(" ", "")
    }
}