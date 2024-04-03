import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.FileWriter
import java.io.InputStreamReader

object Result {
    fun kangaroo(x1: Int, v1: Int, x2: Int, v2: Int): String {
        return if (v1 > v2 && (x2 - x1) % (v1 - v2) == 0) {
            "YES"
        } else {
            "NO"
        }
    }
}

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