impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut students = students;
        let mut sandwiches = sandwiches;
        let mut i = 0;
        while i < students.len() {
            if students[i] == sandwiches[0] {
                students.remove(i);
                sandwiches.remove(0);
                i = 0;
            } else {
                i += 1;
            }
        }
        students.len() as i32
    }
}
