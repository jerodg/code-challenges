/**
 * This class provides a solution for the problem of removing k digits from a number to get the smallest possible number.
 */
class Solution {
    /**
     * This function removes k digits from the input number to get the smallest possible number.
     * @param num The input number as a string.
     * @param k The number of digits to remove.
     * @return The smallest possible number after removing k digits.
     */
    fun removeKdigits(num: String, k: Int): String {
        // If the length of the number is equal to k, return "0"
        if (num.length == k) return "0"

        // Initialize a mutable list to use as a stack
        val stack = mutableListOf<Char>()

        // Initialize a counter with the value of k
        var count = k

        // Iterate over the indices of the number
        for (i in num.indices) {
            // While the counter is greater than 0, the stack is not empty, and the last element of the stack is greater than the current digit
            while (count > 0 && stack.isNotEmpty() && stack.last() > num[i]) {
                // Remove the last element from the stack and decrement the counter
                stack.removeAt(stack.size - 1)
                count--
            }
            // Add the current digit to the stack
            stack.add(num[i])
        }

        // While the counter is greater than 0
        while (count > 0) {
            // Remove the last element from the stack and decrement the counter
            stack.removeAt(stack.size - 1)
            count--
        }

        // Initialize a StringBuilder to build the result
        val sb = StringBuilder()

        // Initialize a flag for leading zeros
        var leadingZero = true

        // Iterate over the indices of the stack
        for (i in stack.indices) {
            // If the flag for leading zeros is true and the current digit is '0', skip this iteration
            if (leadingZero && stack[i] == '0') continue
            // Set the flag for leading zeros to false
            leadingZero = false
            // Append the current digit to the result
            sb.append(stack[i])
        }

        // If the result is empty, return "0", otherwise return the result as a string
        return if (sb.isEmpty()) "0" else sb.toString()
    }
}
