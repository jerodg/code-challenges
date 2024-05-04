/**
 * @fileoverview This module provides a function to count the number of students that cannot eat a sandwich.
 */
/**
 * Counts the number of students that cannot eat a sandwich.
 * @param {number[]} students - An array where students[i] is the preference of the ith student.
 * @param {number[]} sandwiches - An array where sandwiches[i] is the type of the ith sandwich.
 * @return {number} - The number of students that cannot eat a sandwich.
 */
let countStudents = function (students, sandwiches) {
    // Array to keep track of the count of each type of student
    let count = [0, 0];
    // Count the number of each type of student
    students.forEach((student) => count[student]++);
    for (let sandwich of sandwiches) {
        // If there are no students that prefer the current type of sandwich, break the loop
        if (0 === count[sandwich]) {
            break;
        }
        // Decrease the count of the current type of student
        count[sandwich]--;
    }
    // Return the total number of students that cannot eat a sandwich
    return count[0] + count[1];
};
