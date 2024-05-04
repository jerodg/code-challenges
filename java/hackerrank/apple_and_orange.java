import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

enum Result {
    ;

    /*
     * Complete the 'countApplesAndOranges' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER s
     *  2. INTEGER t
     *  3. INTEGER a
     *  4. INTEGER b
     *  5. INTEGER_ARRAY apples
     *  6. INTEGER_ARRAY oranges
     */

    public static void countApplesAndOranges(
            final int s,
            final int t,
            final int a,
            final int b,
            final List<Integer> apples,
            final List<Integer> oranges) {
        final int numApple = apples.size();
        final int numOrange = oranges.size();
        int appleCount = 0;
        int orangeCount = 0;
        for (int apple = 0; apple < numApple; apple++) {
            final int appDist = a + apples.get(apple);
            if (appDist >= s && appDist <= t) {
                appleCount++;
            }
        }
        for (int orange = 0; orange < numOrange; orange++) {
            final int orangeDist = b + oranges.get(orange);
            if (orangeDist >= s && orangeDist <= t) {
                orangeCount++;
            }
        }

        System.out.printf("%d%n%d%n", appleCount, orangeCount);
    }
}

public class Solution {
    public static void main(final String[] args) throws IOException {
        final BufferedReader bufferedReader =
                new BufferedReader(
                        new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));

        final String[] firstMultipleInput =
                bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        final int s = Integer.parseInt(firstMultipleInput[0]);

        final int t = Integer.parseInt(firstMultipleInput[1]);

        final String[] secondMultipleInput =
                bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        final int a = Integer.parseInt(secondMultipleInput[0]);

        final int b = Integer.parseInt(secondMultipleInput[1]);

        final String[] thirdMultipleInput =
                bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        final int m = Integer.parseInt(thirdMultipleInput[0]);

        final int n = Integer.parseInt(thirdMultipleInput[1]);

        final List<Integer> apples =
                Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

        final List<Integer> oranges =
                Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList());

        Result.countApplesAndOranges(s, t, a, b, apples, oranges);

        bufferedReader.close();
    }
}
