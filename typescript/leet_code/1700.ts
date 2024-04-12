/**
 * @fileoverview This module contains a solution for the "Number of Students Unable to Eat Lunch" problem from LeetCode.
 * The problem is solved by using a queue to simulate the process of students in line.
 */

/**
 * Function to count the number of students who are unable to eat lunch.
 * The function iterates over the students and sandwiches arrays and uses a queue to simulate the process of students in line.
 * If the student at the front of the line likes the sandwich at the front of the line, the student eats the sandwich and leaves
 * the line. Otherwise, the student goes to the back of the line. The process continues until all students have eaten or all
 * remaining students in the line do not like the sandwich at the front of the line.
 *
 * @param {number[]} students - The students in line, represented as an array of numbers where 0 represents a student that likes
 *     type 0 sandwiches and 1 represents a student that likes type 1 sandwiches.
 * @param {number[]} sandwiches - The sandwiches, represented as an array of numbers where 0 represents a type 0 sandwich and 1
 *     represents a type 1 sandwich.
 * @returns {number} The number of students who are unable to eat lunch.
 */
function countStudents(students: number[], sandwiches: number[]): number {
    // Initialize the total number of students, the pointer to the current sandwich, and the counter for unsuccessful attempts to
    // eat a sandwich
    let totalStudents: number = students.length;
    let sandwichPointer: number = 0;
    let unsuccessfulAttempts: number = 0;

    // While there are students in line and the number of unsuccessful attempts is less than the total number of students
    while (students.length > 0 && unsuccessfulAttempts < totalStudents) {
        // Get the student at the front of the line
        let student: number = students.shift() as number;
        // If the student likes the sandwich at the front of the line
        if (student === sandwiches[sandwichPointer]) {
            // The student eats the sandwich and leaves the line, and the pointer to the current sandwich is incremented
            sandwichPointer++;
            // The counter for unsuccessful attempts is reset
            unsuccessfulAttempts = 0;
        } else {
            // If the student does not like the sandwich at the front of the line, the student goes to the back of the line
            students.push(student);
            // The counter for unsuccessful attempts is incremented
            unsuccessfulAttempts++;
        }
    }
    // Return the number of students who are unable to eat lunch
    return students.length;
}
