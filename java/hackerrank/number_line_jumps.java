import java.io.*;

enum Result {
    ;

    public static String kangaroo(final int x1, final int v1, final int x2, final int v2) {
        if (v1 > v2) {
            if (0 == (x2 - x1) % (v1 - v2)) {
                return "YES";
            }
        }
        return "NO";
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

        final int x1 = Integer.parseInt(firstMultipleInput[0]);

        final int v1 = Integer.parseInt(firstMultipleInput[1]);

        final int x2 = Integer.parseInt(firstMultipleInput[2]);

        final int v2 = Integer.parseInt(firstMultipleInput[3]);

        final String result = Result.kangaroo(x1, v1, x2, v2);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
