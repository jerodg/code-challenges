class Solution {
    func countStudents(_ students: [Int], _ sandwiches: [Int]) -> Int {
        var students = students
        var sandwiches = sandwiches
        var i = 0
        while i < students.count {
            if students[0] == sandwiches[0] {
                students.removeFirst()
                sandwiches.removeFirst()
                i = 0
            } else {
                students.append(students.removeFirst())
                i += 1
            }
        }
        return students.count
    }
}
