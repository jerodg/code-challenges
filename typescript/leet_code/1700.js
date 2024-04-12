function countStudents(students, sandwiches) {
    var totalStudents = students.length;
    var sandwichPointer = 0;
    var unsuccessfulAttempts = 0;
    while (students.length > 0 && unsuccessfulAttempts < totalStudents) {
        var student = students.shift();
        if (student === sandwiches[sandwichPointer]) {
            sandwichPointer++;
            unsuccessfulAttempts = 0;
        }
        else {
            students.push(student);
            unsuccessfulAttempts++;
        }
    }
    return students.length;
}
