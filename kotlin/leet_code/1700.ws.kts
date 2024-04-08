class Solution {
    fun countStudents(students: IntArray, sandwiches: IntArray): Int {
        val studentsCount = students.size
        val sandwichesCount = sandwiches.size
        val studentsMap = mutableMapOf<Int, Int>()
        students.forEach { student ->
            studentsMap[student] = studentsMap.getOrDefault(student, 0) + 1
        }
        var i = 0
        var j = 0
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