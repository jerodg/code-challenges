/**
 * This Kotlin module provides a solution for the CodeWars problem "Convert number to reversed array of digits".
 * The problem is about converting a given number into a reversed array of its digits.
 *
 * @module code_wars/convert_number_to_reversed_array_of_digits.ws.kts
 */

/**
 * Kata object provides a method to convert a number into a reversed array of its digits.
 */
object Kata {

    /**
     * This function converts a number into a reversed array of its digits.
     *
     * @param n The input number to be converted.
     * @return An integer array representing the reversed array of the digits of the input number.
     *
     * The function first converts the input number into a string, then reverses the string.
     * It then creates an integer array of the same length as the reversed string.
     * It iterates over the indices of the reversed string, and for each index, it converts the character at that index into a numeric value and assigns it to the corresponding index in the integer array.
     * Finally, it returns the integer array.
     *
     * Example usage:
     * val n = 12345L
     * val result = Kata.digitize(n)
     * // result will be intArrayOf(5, 4, 3, 2, 1) as these are the digits of the input number in reverse order
     */
    fun digitize(n: Long): IntArray {
        val str = n.toString().reversed()
        val result = IntArray(str.length)
        for (i in str.indices) {
            result[i] = Character.getNumericValue(str[i])
        }
        return result
    }
}
