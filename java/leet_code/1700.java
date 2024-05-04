/**
 * This class provides a solution for the problem of counting the number of students that cannot eat
 * a sandwich.
 * The problem is solved by counting the number of students that prefer each type of sandwich and
 * then iterating over the sandwiches.
 * If the current sandwich is preferred by any student, the count of students that prefer this type
 * of sandwich is decreased.
 * If the current sandwich is not preferred by any student, the iteration is stopped.
 * The count of students that cannot eat a sandwich is the sum of the counts of students that prefer
 * each type of sandwich.
 */
class Solution {

    /**
     * Counts the number of students that cannot eat a sandwich.
     *
     * @param students   An array of integers representing the preference of each student. Each
     *                   integer is either 0 or 1, where 0 means the student prefers the type 0
     *                   sandwich and 1 means the student prefers the type 1 sandwich.
     * @param sandwiches An array of integers representing the type of each sandwich. Each integer
     *                   is either 0 or 1, where 0 means the sandwich is of type 0 and 1 means the
     *                   sandwich is of type 1.
     *
     * @return The number of students that cannot eat a sandwich. It is a non-negative integer.
     */
    public int countStudents(final int[] students, final int[] sandwiches) {
        // Initialize an array to count the number of students that prefer each type of sandwich
        final int[] count = new int[2];

        // Count the number of students that prefer each type of sandwich
        for (final int student : students) {
            count[student]++;
        }

        // Iterate over the sandwiches
        for (final int sandwich : sandwiches) {
            // If the current sandwich is not preferred by any student, stop the iteration
            if (0 == count[sandwich]) {
                break;
            }

            // Decrease the count of students that prefer the current sandwich
            count[sandwich]--;
        }

        // Return the sum of the counts of students that prefer each type of sandwich
        return count[0] + count[1];
    }
}
