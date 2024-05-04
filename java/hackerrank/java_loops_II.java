/**
 * This module is a solution to the Java Loops II problem on HackerRank.
 * It reads the number of test cases and the test cases from the standard input,
 * calculates the series for each test case, and writes the results to the standard output.
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads the number of test cases and the test cases from the standard input,
 * calculates the series for each test case, and writes the results to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads the number of test cases and the test cases from the standard input,
     * calculates the series for each test case, and writes the results to the standard output.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Read the number of test cases
        final int t = in.nextInt();

        // Process each test case
        for (int i = 0; i < t; i++) {
            // Read the test case
            final int a = in.nextInt();
            final int b = in.nextInt();
            final int n = in.nextInt();

            // Initialize the sum
            int sum = a;

            // Calculate the series for the test case
            for (int j = 0; j < n; j++) {
                sum += Math.pow(2, j) * b;

                // Write the result to the standard output
                System.out.print(sum + " ");
            }

            // Write a newline to the standard output
            System.out.println();
        }

        // Close the Scanner
        in.close();
    }
}
