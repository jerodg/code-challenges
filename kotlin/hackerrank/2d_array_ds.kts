/**
 * This Kotlin module provides a solution for the HackerRank problem "2D Array - DS".
 * The solution calculates the maximum hourglass sum in a 6x6 2D array.
 *
 * @module hackerrank/2d_array_ds.ws.kts
 */

/**
 * This function calculates the maximum hourglass sum in a 6x6 2D array.
 *
 * @param arr The input 2D array of integers where the hourglass sums are to be calculated.
 * @return An integer representing the maximum hourglass sum in the input 2D array.
 *
 * The function uses a nested loop to iterate over the hourglasses in the 2D array.
 * For each hourglass, it calculates the sum of its elements and updates the maximum hourglass sum if the current hourglass sum is greater.
 * An hourglass in the 2D array is a subset of numbers with indices falling into this pattern: (i-1, j-1), (i-1, j), (i-1, j+1), (i, j), (i+1, j-1), (i+1, j), (i+1, j+1).
 *
 * Example usage:
 * val arr = arrayOf(
 *     arrayOf(1, 1, 1, 0, 0, 0),
 *     arrayOf(0, 1, 0, 0, 0, 0),
 *     arrayOf(1, 1, 1, 0, 0, 0),
 *     arrayOf(0, 0, 2, 4, 4, 0),
 *     arrayOf(0, 0, 0, 2, 0, 0),
 *     arrayOf(0, 0, 1, 2, 4, 0)
 * )
 * val maxSum = hourglassSum(arr)
 * // maxSum will be 19 as the maximum hourglass sum is 19
 */
fun hourglassSum(arr: Array<Array<Int>>): Int {
    var maxSum = Int.MIN_VALUE
    for (i in 1 until 5) {
        for (j in 1 until 5) {
            val top = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1]
            val mid = arr[i][j]
            val bottom = arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            val hourglassSum = top + mid + bottom
            maxSum = kotlin.math.max(maxSum, hourglassSum)
        }
    }
    return maxSum
}

/**
 * The main function reads a 6x6 2D array of integers from the standard input, calculates the maximum hourglass sum in the 2D array, and prints it to the standard output.
 */
fun main(args: Array<String>) {

    val arr = Array<Array<Int>>(6, { Array<Int>(6, { 0 }) })

    for (i in 0 until 6) {
        arr[i] = readLine()!!.trimEnd().split(" ").map { it.toInt() }.toTypedArray()
    }

    val result = hourglassSum(arr)

    println(result)
}
