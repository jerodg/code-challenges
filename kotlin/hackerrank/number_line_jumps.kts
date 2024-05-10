import java.io.BufferedReader
import java.io.BufferedWriter

/**
 * This Kotlin module provides a solution for the HackerRank problem "Number Line Jumps".
 * The problem is about determining if two kangaroos on a number line can land at the same spot after making jumps of fixed lengths.
 *
 * @module hackerrank/number_line_jumps.ws.kts
 */

/**
 * Result object provides a method to determine if two kangaroos can land at the same spot.
 */
object Result {

    /**
     * This function determines if two kangaroos can land at the same spot.
     *
     * @param x1 The initial position of the first kangaroo.
     * @param v1 The jump distance of the first kangaroo.
     * @param x2 The initial position of the second kangaroo.
     * @param v2 The jump distance of the second kangaroo.
     * @return A string "YES" if the two kangaroos can land at the same spot, or "NO" otherwise.
     *
     * The function checks if the first kangaroo jumps farther than the second kangaroo and if the difference in the initial positions is divisible by the difference in the jump distances.
     * If both conditions are true, the kangaroos will land at the same spot, so the function returns "YES". Otherwise, it returns "NO".
     *
     * Example usage:
     * val result = Result.kangaroo(0, 3, 4, 2)
     * // result will be "YES" as the two kangaroos will land at the same spot after 4 jumps
     */
    fun kangaroo(x1: Int, v1: Int, x2: Int, v2: Int): String {
        return if (v1 > v2 && (x2 - x1) % (v1 - v2) == 0) {
            "YES"
        } else {
            "NO"
        }
    }
}

/**
 * The main function reads the initial positions and the jump distances of the two kangaroos from the standard input, calls the function `kangaroo` with these inputs, and writes the returned string to a file specified by the environment variable "OUTPUT_PATH".
 */
fun main(args: Array<String>) {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val writer = BufferedWriter(FileWriter(System.getenv("OUTPUT_PATH")))

    val firstMultipleInput = reader.readLine().trimEnd().split(" ")

    val x1 = firstMultipleInput[0].toInt()

    val v1 = firstMultipleInput[1].toInt()

    val x2 = firstMultipleInput[2].toInt()

    val v2 = firstMultipleInput[3].toInt()

    val result = Result.kangaroo(x1, v1, x2, v2)

    writer.write(result)
    writer.newLine()

    reader.close()
    writer.close()
}
