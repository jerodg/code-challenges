/**
 * This Kotlin module provides a solution for the HackerRank problem "Apple and Orange".
 * The problem is about counting the number of apples and oranges that fall on Sam's house, given the locations of the trees and the house, and the distances each fruit falls from its tree.
 *
 * @module hackerrank/apple_and_orange.ws.kts
 */

/**
 * This function counts the number of apples and oranges that fall on Sam's house.
 *
 * @param s The integer location of the start of Sam's house.
 * @param t The integer location of the end of Sam's house.
 * @param a The integer location of the apple tree.
 * @param b The integer location of the orange tree.
 * @param apples The integer array distances at which each apple falls from the apple tree.
 * @param oranges The integer array distances at which each orange falls from the orange tree.
 *
 * The function prints two lines to the standard output:
 * 1. The first line contains the number of apples that fall on Sam's house.
 * 2. The second line contains the number of oranges that fall on Sam's house.
 *
 * An apple or an orange falls on Sam's house if its location (the location of the tree plus the distance it falls) is between the start and the end of Sam's house, inclusive.
 *
 * Example usage:
 * val s = 7
 * val t = 10
 * val a = 4
 * val b = 12
 * val apples = arrayOf(2, 3, -4)
 * val oranges = arrayOf(3, -2, -4)
 * countApplesAndOranges(s, t, a, b, apples, oranges)
 * // This will print:
 * // 1
 * // 2
 */
fun countApplesAndOranges(s: Int, t: Int, a: Int, b: Int, apples: Array<Int>, oranges: Array<Int>): Unit {
    println(apples.count { d -> s <= a + d && a + d <= t })
    println(oranges.count { d -> s <= b + d && b + d <= t })
}

/**
 * The main function reads the locations of the start and the end of Sam's house, the locations of the apple and the orange trees, and the distances each apple and orange falls from its tree from the standard input.
 * It then calls the function countApplesAndOranges with these inputs.
 */
fun main(args: Array<String>) {

    val first_multiple_input = readLine()!!.trimEnd().split(" ")

    val s = first_multiple_input[0].toInt()

    val t = first_multiple_input[1].toInt()

    val second_multiple_input = readLine()!!.trimEnd().split(" ")

    val a = second_multiple_input[0].toInt()

    val b = second_multiple_input[1].toInt()

    val third_multiple_input = readLine()!!.trimEnd().split(" ")

    val m = third_multiple_input[0].toInt()

    val n = third_multiple_input[1].toInt()

    val apples = readLine()!!.trimEnd().split(" ").map { it.toInt() }.toTypedArray()

    val oranges = readLine()!!.trimEnd().split(" ").map { it.toInt() }.toTypedArray()

    countApplesAndOranges(s, t, a, b, apples, oranges)
}
