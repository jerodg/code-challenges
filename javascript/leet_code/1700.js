/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
let countStudents = function (students, sandwiches) {
    let count = [0, 0];
    students.forEach((student) => count[student]++);
    for (let sandwich of sandwiches) {
        if (count[sandwich] === 0) break;
        count[sandwich]--;
    }
    return count[0] + count[1];
};
