import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

enum Result {
    ;

    /*
     * Complete the 'dynamicArray' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static List<Integer> dynamicArray(final int n, final List<List<Integer>> queries) {
        final List<List<Integer>> seqList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            seqList.add(new ArrayList<>());
        }
        int lastAnswer = 0;
        final List<Integer> result = new ArrayList<>();
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
        return result;
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

        final String[] firstMultipleInput =
                bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        final int n = Integer.parseInt(firstMultipleInput[0]);

        final int q = Integer.parseInt(firstMultipleInput[1]);

        final List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q)
                .forEach(
                        i -> {
                            try {
                                queries.add(
                                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                                .map(Integer::parseInt)
                                                .collect(toList()));
                            } catch (final IOException ex) {
                                throw new RuntimeException(ex);
                            }
                        });

        final List<Integer> result = Result.dynamicArray(n, queries);

        bufferedWriter.write(result.stream().map(Object::toString).collect(joining("\n")) + "\n");

        bufferedReader.close();
        bufferedWriter.close();
    }
}
