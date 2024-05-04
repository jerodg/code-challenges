/**
 * This module is a solution to the Dynamic Array problem on HackerRank.
 * It reads the number of sequences, the queries from the standard input,
 * performs the queries on the sequences, and writes the results to a file.
 */

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

/**
 * This enum encapsulates the logic for performing the queries on the sequences.
 */
enum Result {
    ;

    /**
     * Performs the queries on the sequences.
     *
     * @param n       the number of sequences
     * @param queries the queries to perform on the sequences
     *
     * @return the results of the queries as a List of Integers
     */
    public static List<Integer> dynamicArray(final int n, final List<List<Integer>> queries) {
        // Initialize the sequences
        final List<List<Integer>> seqList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            seqList.add(new ArrayList<>());
        }

        int lastAnswer = 0;
        final List<Integer> result = new ArrayList<>();

        // Perform the queries on the sequences
        for (final List<Integer> query : queries) {
            final int queryType = query.get(0);
            final int x = query.get(1);
            final int y = query.get(2);
            final int index = (x ^ lastAnswer) % n;
            final List<Integer> seq = seqList.get(index);
            if (1 == queryType) {
                seq.add(y);
            } else {
                lastAnswer = seq.get(y % seq.size());
                result.add(lastAnswer);
            }
        }

        // Return the results of the queries
        return result;
    }
}

/**
 * This class contains the main method for the program.
 * It reads the number of sequences, the queries from the standard input,
 * performs the queries on the sequences, and writes the results to a file.
 */
public class Solution {
    /**
     * The main method for the program.
     * It reads the number of sequences, the queries from the standard input,
     * performs the queries on the sequences, and writes the results to a file.
     *
     * @param args the command-line arguments for the program
     *
     * @throws IOException if an I/O error occurs
     */
    public static void main(final String[] args) throws IOException {
        // Initialize the BufferedReader and BufferedWriter
        final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));
        final BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH"), java.nio.charset.StandardCharsets.UTF_8));

        // Read the number of sequences and the number of queries
        final String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
        final int n = Integer.parseInt(firstMultipleInput[0]);
        final int q = Integer.parseInt(firstMultipleInput[1]);

        // Initialize the queries
        final List<List<Integer>> queries = new ArrayList<>();

        // Read the queries from the standard input
        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" ")).map(Integer::parseInt).collect(toList()));
            } catch (final IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        // Perform the queries on the sequences
        final List<Integer> result = Result.dynamicArray(n, queries);

        // Write the results to the file
        bufferedWriter.write(result.stream().map(Object::toString).collect(joining("\n")) + "\n");

        // Close the BufferedReader and BufferedWriter
        bufferedReader.close();
        bufferedWriter.close();
    }
}
