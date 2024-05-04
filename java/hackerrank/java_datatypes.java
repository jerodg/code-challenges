/**
 * This module is a solution to the Java Datatypes problem on HackerRank.
 * It reads the number of test cases and the test cases from the standard input,
 * determines the data types that each test case can be fitted into, and writes the results to the standard output.
 *
 * @author jerodg
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads the number of test cases and the test cases from the standard input,
 * determines the data types that each test case can be fitted into, and writes the results to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads the number of test cases and the test cases from the standard input,
     * determines the data types that each test case can be fitted into, and writes the results to the standard output.
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
            try {
                // Read the test case
                final long x = in.nextLong();

                // Print the data types that the test case can be fitted into
                System.out.println(x + " can be fitted in:");
                if (Byte.MIN_VALUE <= x && Byte.MAX_VALUE >= x) {
                    System.out.println("* byte");
                }
                if (Short.MIN_VALUE <= x && Short.MAX_VALUE >= x) {
                    System.out.println("* short");
                }
                if (Integer.MIN_VALUE <= x && Integer.MAX_VALUE >= x) {
                    System.out.println("* int");
                }
                if (Long.MIN_VALUE <= x && Long.MAX_VALUE >= x) {
                    System.out.println("* long");
                }
            } catch (final Exception e) {
                // Handle the exception when the test case can't be fitted into any data type
                System.out.println(in.next() + " can't be fitted anywhere.");
            }
        }

        // Close the Scanner
        in.close();
    }
}
