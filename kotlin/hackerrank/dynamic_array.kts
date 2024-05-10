/**
 * This Kotlin module provides a solution for the HackerRank problem "Dynamic Array".
 * The problem is about creating a list of sequences, performing two types of queries on them, and maintaining a variable `lastAnswer`.
 *
 * @module hackerrank/dynamic_array.ws.kts
 */

/**
 * This function performs the queries on the sequences and returns the values of `lastAnswer` after each type 2 query.
 *
 * @param n The number of sequences.
 * @param queries The 2D array of queries, where each query is an array of three integers. The first integer is the type of the query (1 or 2). The second and third integers are `x` and `y`, respectively, which are used in the query operations.
 * @return An array of integers representing the values of `lastAnswer` after each type 2 query.
 *
 * The function creates a list of `n` empty sequences and initializes `lastAnswer` to 0.
 * It then iterates over the queries. For each query, it calculates the index of the sequence to be operated on as `(x xor lastAnswer) % n`.
 * If the query type is 1, it appends `y` to the calculated sequence.
 * If the query type is 2, it updates `lastAnswer` to the `y % size`-th value of the calculated sequence and appends `lastAnswer` to the result.
 * Finally, it returns the result as an array.
 *
 * Example usage:
 * val n = 2
 * val queries = arrayOf(
 *     arrayOf(1, 0, 5),
 *     arrayOf(1, 1, 7),
 *     arrayOf(1, 0, 3),
 *     arrayOf(2, 1, 0),
 *     arrayOf(2, 1, 1)
 * )
 * val result = dynamicArray(n, queries)
 * // result will be arrayOf(7, 3) as these are the values of `lastAnswer` after each type 2 query
 */
fun dynamicArray(n: Int, queries: Array<Array<Int>>): Array<Int> {
    val seqList = Array(n) { mutableListOf<Int>() }
    var lastAnswer = 0
    val result = mutableListOf<Int>()
    for (query in queries) {
        val x = query[1]
        val y = query[2]
        val seq = (x xor lastAnswer) % n
        if (query[0] == 1) {
            seqList[seq].add(y)
        } else {
            lastAnswer = seqList[seq][y % seqList[seq].size]
            result.add(lastAnswer)
        }
    }
    return result.toTypedArray()
}

/**
 * The main function reads the number of sequences and the queries from the standard input, calls the function `dynamicArray` with these inputs, and prints the returned values of `lastAnswer` to the standard output.
 */
fun main(args: Array<String>) {
    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val n = first_multiple_input[0].toInt()

    val q = first_multiple_input[1].toInt()

    val queries = Array<Array<Int>>(q, { Array<Int>(3, { 0 }) })

    for (i in 0 until q) {
        queries[i] = readLine()!!.trimEnd().split(" ").map { it.toInt() }.toTypedArray()
    }

    val result = dynamicArray(n, queries)

    println(result.joinToString("\n"))
}
