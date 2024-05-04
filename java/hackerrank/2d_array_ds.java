import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

enum Result {
    ;

    /*
     * Complete the 'hourglassSum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int hourglassSum(final List<List<Integer>> arr) {
        int maxSum = Integer.MIN_VALUE;
        for (int i = 1; 5 > i; i++) {
            for (int j = 1; 5 > j; j++) {
                final int top =
                        arr.get(i - 1).get(j - 1) + arr.get(i - 1).get(j) + arr.get(i - 1).get(j + 1);
                final int mid = arr.get(i).get(j);
                final int bottom =
                        arr.get(i + 1).get(j - 1) + arr.get(i + 1).get(j) + arr.get(i + 1).get(j + 1);
                final int hourglassSum = top + mid + bottom;
                maxSum = Math.max(maxSum, hourglassSum);
            }
        }
        return maxSum;
    }
}

public class Solution {
    public static void main(final String[] args) throws IOException {
        final BufferedReader bufferedReader =
                new BufferedReader(
                        new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));
        final BufferedWriter bufferedWriter =
                new BufferedWriter(
                        new FileWriter(System.getenv("OUTPUT_PATH"), java.nio.charset.StandardCharsets.UTF_8));

        final List<List<Integer>> arr = new ArrayList<>();

        IntStream.range(0, 6)
                .forEach(
                        i -> {
                            try {
                                arr.add(
                                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                                .map(Integer::parseInt)
                                                .collect(toList()));
                            } catch (final IOException ex) {
                                throw new RuntimeException(ex);
                            }
                        });

        final int result = Result.hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
