/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
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
