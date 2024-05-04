/**
 * This module is a solution to the Java Loops I problem on HackerRank.
 * It reads an integer from the standard input, calculates the first ten multiples of the integer,
 * and writes the results to the standard output.
 *
 * @author jerodg
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * This class contains the main method for the program.
 * It reads an integer from the standard input, calculates the first ten multiples of the integer,
 * and writes the results to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads an integer from the standard input, calculates the first ten multiples of the integer,
     * and writes the results to the standard output.
     *
     * @param args the command-line arguments for the program
     *
     * @throws IOException if an I/O error occurs
     */
    public static void main(final String[] args) throws IOException {
        // Initialize the BufferedReader
        final BufferedReader bufferedReader =
                new BufferedReader(
                        new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));

        // Read the integer from the standard input
        final int N = Integer.parseInt(bufferedReader.readLine().trim());

        // Calculate the first ten multiples of the integer
        for (int i = 1; 10 >= i; i++) {
            // Write the result to the standard output
            System.out.printf("%d x %d = %d\n", N, i, N * i);
        }

        // Close the BufferedReader
        bufferedReader.close();
    }
}
