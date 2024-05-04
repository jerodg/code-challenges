/**
 * This module is a solution to the 2D Array - DS problem on HackerRank.
 * It reads a 2D array from the standard input, calculates the maximum hourglass sum, and writes the result to a file.
 * An hourglass in this context is a subset of values with indices falling into this pattern in the 2D array:
 * a b c
 * d
 * e f g
 * The maximum hourglass sum is the largest possible sum of an hourglass.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

/**
 * This enum encapsulates the logic for calculating the maximum hourglass sum in a 2D array.
 */
enum Result {
    ;

    /**
     * Calculates the maximum hourglass sum in the given 2D array.
     * An hourglass is a subset of values with indices falling into this pattern in the 2D array:
     * a b c
     *   d
     * e f g
     * The maximum hourglass sum is the largest possible sum of an hourglass.
     *
     * @param arr the 2D array to calculate the maximum hourglass sum in, represented as a List of Lists of Integers
     * @return the maximum hourglass sum as an Integer
     */
    public static int hourglassSum(final List<List<Integer>> arr) {
        // Initialize the maximum sum to the smallest possible integer
        int maxSum = Integer.MIN_VALUE;

        // Iterate over the 2D array, skipping the first and last row and column
        for (int i = 1; 5 > i; i++) {
            for (int j = 1; 5 > j; j++) {
                // Calculate the sum of the top, middle, and bottom of the hourglass
                final int top = arr.get(i - 1).get(j - 1) + arr.get(i - 1).get(j) + arr.get(i - 1).get(j + 1);
                final int mid = arr.get(i).get(j);
                final int bottom = arr.get(i + 1).get(j - 1) + arr.get(i + 1).get(j) + arr.get(i + 1).get(j + 1);

                // Calculate the sum of the hourglass
                final int hourglassSum = top + mid + bottom;

                // Update the maximum sum if the current hourglass sum is greater
                maxSum = Math.max(maxSum, hourglassSum);
            }
        }

        // Return the maximum hourglass sum
        return maxSum;
    }
}

/**
 * This class contains the main method for the program.
 * It reads a 2D array from the standard input, calculates the maximum hourglass sum, and writes the result to a file.
 */
public class Solution {
    /**
     * The main method for the program.
     * It reads a 2D array from the standard input, calculates the maximum hourglass sum, and writes the result to a file.
     *
     * @param args the command-line arguments for the program
     * @throws IOException if an I/O error occurs
     */
    public static void main(final String[] args) throws IOException {
        // Initialize the BufferedReader and BufferedWriter
        final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));
        final BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH"), java.nio.charset.StandardCharsets.UTF_8));

        // Initialize the 2D array
        final List<List<Integer>> arr = new ArrayList<>();

        // Read the 2D array from the standard input
        IntStream.range(0, 6).forEach(i -> {
            try {
                arr.add(Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" ")).map(Integer::parseInt).collect(toList()));
            } catch (final IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        // Calculate the maximum hourglass sum
        final int result = Result.hourglassSum(arr);

        // Write the result to the file
        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        // Close the BufferedReader and BufferedWriter
        bufferedReader.close();
        bufferedWriter.close();
    }
}
