function countStudents(students: number[], sandwiches: number[]): number {
    let totalStudents = students.length;
    let sandwichPointer = 0;
    let unsuccessfulAttempts = 0;

    while (students.length > 0 && unsuccessfulAttempts < totalStudents) {
        let student = students.shift();
        if (student === sandwiches[sandwichPointer]) {
            sandwichPointer++;
            unsuccessfulAttempts = 0;
        } else {
            students.push(student);
            unsuccessfulAttempts++;
        }
    }

    return students.length;
}
