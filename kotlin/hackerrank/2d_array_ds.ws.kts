/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
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

fun main(args: Array<String>) {

    val arr = Array<Array<Int>>(6, { Array<Int>(6, { 0 }) })

    for (i in 0 until 6) {
        arr[i] = readLine()!!.trimEnd().split(" ").map { it.toInt() }.toTypedArray()
    }

    val result = hourglassSum(arr)

    println(result)
}
