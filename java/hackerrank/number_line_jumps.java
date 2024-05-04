/**
 * This module is a solution to the Number Line Jumps problem on HackerRank.
 * It calculates if two kangaroos on a number line will land at the same spot at the same time.
 *
 * @author jerodg
 */

import java.io.*;

/**
 * This enum contains the method to calculate if two kangaroos on a number line will land at the same spot at the same time.
 */
enum Result {
    ;

    /**
     * This method calculates if two kangaroos on a number line will land at the same spot at the same time.
     *
     * @param x1 the starting position of the first kangaroo
     * @param v1 the jump distance of the first kangaroo
     * @param x2 the starting position of the second kangaroo
     * @param v2 the jump distance of the second kangaroo
     *
     * @return "YES" if the kangaroos will land at the same spot at the same time, "NO" otherwise
     */
    public static String kangaroo(final int x1, final int v1, final int x2, final int v2) {
        if (v1 > v2) {
            if (0 == (x2 - x1) % (v1 - v2)) {
                return "YES";
            }
        }
        return "NO";
    }
}

/**
 * This class contains the main method for the program.
 * It reads the starting positions and jump distances of two kangaroos from the standard input,
 * calculates if the kangaroos will land at the same spot at the same time, and writes the result to the standard output.
 */
public class Solution {
    /**
     * The main method for the program.
     * It reads the starting positions and jump distances of two kangaroos from the standard input,
     * calculates if the kangaroos will land at the same spot at the same time, and writes the result to the standard output.
     *
     * @param args the command-line arguments for the program
     *
     * @throws IOException if an I/O error occurs
     */
    public static void main(final String[] args) throws IOException {
        // Initialize the BufferedReader and BufferedWriter
        final BufferedReader bufferedReader =
                new BufferedReader(
                        new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));
        final BufferedWriter bufferedWriter =
                new BufferedWriter(
                        new FileWriter(System.getenv("OUTPUT_PATH"), java.nio.charset.StandardCharsets.UTF_8));

        // Read the starting positions and jump distances of the kangaroos
        final String[] firstMultipleInput =
                bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        final int x1 = Integer.parseInt(firstMultipleInput[0]);
        final int v1 = Integer.parseInt(firstMultipleInput[1]);
        final int x2 = Integer.parseInt(firstMultipleInput[2]);
        final int v2 = Integer.parseInt(firstMultipleInput[3]);

        // Calculate if the kangaroos will land at the same spot at the same time
        final String result = Result.kangaroo(x1, v1, x2, v2);

        // Write the result to the standard output
        bufferedWriter.write(result);
        bufferedWriter.newLine();

        // Close the BufferedReader and BufferedWriter
        bufferedReader.close();
        bufferedWriter.close();
    }
}
