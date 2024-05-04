/**
 * This module is a solution to the Apple and Orange problem on HackerRank.
 * It reads the positions of the house, the trees, and the distances of the fruits from the trees from the standard input,
 * calculates the number of apples and oranges that fall on the house, and writes the results to the standard output.
 *
 * @author jerodg
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

/**
 * This enum encapsulates the logic for calculating the number of apples and oranges that fall on the house.
 */
enum Result {
    ;

    /**
     * Calculates the number of apples and oranges that fall on the house.
     *
     * @param s       the start point of the house
     * @param t       the end point of the house
     * @param a       the location of the apple tree
     * @param b       the location of the orange tree
     * @param apples  the distances at which each apple falls from the apple tree
     * @param oranges the distances at which each orange falls from the orange tree
     */
    public static void countApplesAndOranges(
            final int s,
            final int t,
            final int a,
            final int b,
            final List<Integer> apples,
            final List<Integer> oranges) {
        // Initialize the counts of apples and oranges that fall on the house
        int appleCount = 0;
        int orangeCount = 0;

        // Calculate the number of apples that fall on the house
        for (final int apple : apples) {
            final int appDist = a + apple;
            if (appDist >= s && appDist <= t) {
                appleCount++;
            }
        }

        // Calculate the number of oranges that fall on the house
        for (final int orange : oranges) {
            final int orangeDist = b + orange;
            if (orangeDist >= s && orangeDist <= t) {
                orangeCount++;
            }
        }

        // Print the counts of apples and oranges that fall on the house
        System.out.printf("%d%n%d%n", appleCount, orangeCount);
    }
}

/**
 * This class contains the main method for the program.
 * It reads the positions of the house, the trees, and the distances of the fruits from the trees from the standard input,
 * calculates the number of apples and oranges that fall on the house, and writes the results to the standard output.
 */
public class Solution {
    /**
     * The main method for the program.
     * It reads the positions of the house, the trees, and the distances of the fruits from the trees from the standard input,
     * calculates the number of apples and oranges that fall on the house, and writes the results to the standard output.
     *
     * @param args the command-line arguments for the program
     *
     * @throws IOException if an I/O error occurs
     */
    public static void main(final String[] args) throws IOException {
        // Initialize the BufferedReader
        final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));

        // Read the positions of the house
        final String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        final int s = Integer.parseInt(firstMultipleInput[0]);
        final int t = Integer.parseInt(firstMultipleInput[1]);

        // Read the locations of the trees
        final String[] secondMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        final int a = Integer.parseInt(secondMultipleInput[0]);
        final int b = Integer.parseInt(secondMultipleInput[1]);

        // Skip the line that contains the number of apples and oranges
        bufferedReader.readLine();

        // Read the distances at which each apple falls from the apple tree
        final List<Integer> apples = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" ")).map(Integer::parseInt).collect(toList());

        // Read the distances at which each orange falls from the orange tree
        final List<Integer> oranges = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" ")).map(Integer::parseInt).collect(toList());

        // Calculate the number of apples and oranges that fall on the house
        Result.countApplesAndOranges(s, t, a, b, apples, oranges);

        // Close the BufferedReader
        bufferedReader.close();
    }
}
