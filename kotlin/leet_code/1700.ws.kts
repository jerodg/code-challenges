/**
 * This Kotlin module provides a solution for the LeetCode problem 1700. Number of Students Unable to Eat Lunch.
 * The solution calculates the number of students that cannot eat lunch. The students are in a queue and each student either prefers square or circular sandwiches.
 * The sandwiches are stacked in a stack. The student at the front of the queue either eats the sandwich at the top of the stack or skips it if it is not their preferred type.
 * The student who skips the sandwich cannot eat other sandwiches in the stack.
 *
 * @module leet_code/1700.ws.kts
 */

/**
 * Solution class provides a method to calculate the number of students that cannot eat lunch.
 */
class Solution {

    /**
     * This function calculates the number of students that cannot eat lunch.
     *
     * @param students An integer array representing the students in the queue. Each student is represented by an integer where 0 represents a student that prefers square sandwiches and 1 represents a student that prefers circular sandwiches.
     * @param sandwiches An integer array representing the sandwiches in the stack. Each sandwich is represented by an integer where 0 represents a square sandwich and 1 represents a circular sandwich.
     * @return An integer representing the number of students that cannot eat lunch.
     *
     * The function uses a map to keep track of the number of students that prefer each type of sandwich. It iterates over the sandwiches in the stack.
     * If there are students that prefer the sandwich at the top of the stack, it decreases the number of such students in the map and moves to the next sandwich in the stack.
     * If there are no students that prefer the sandwich at the top of the stack, it stops the iteration.
     * Finally, it returns the number of students that cannot eat lunch, which is the difference between the total number of students and the number of sandwiches that have been eaten.
     *
     * Example usage:
     * val solution = Solution()
     * val students = intArrayOf(1,1,0,0)
     * val sandwiches = intArrayOf(0,1,0,1)
     * val studentsUnableToEat = solution.countStudents(students, sandwiches)
     * // studentsUnableToEat will be 0 as all students can eat a sandwich of their preferred type
     */
    fun countStudents(students: IntArray, sandwiches: IntArray): Int {
        val studentsCount = students.size
        val sandwichesCount = sandwiches.size
        val studentsMap = mutableMapOf<Int, Int>()
        students.forEach { student ->
            studentsMap[student] = studentsMap.getOrDefault(student, 0) + 1
        }
        var i = 0
        while (i < sandwichesCount) {
            if (studentsMap.getOrDefault(sandwiches[i], 0) > 0) {
                studentsMap[sandwiches[i]] = studentsMap[sandwiches[i]]!! - 1
                i++
            } else {
                break
            }
        }
        return studentsCount - i
    }
}
