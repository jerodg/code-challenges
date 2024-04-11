import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
  public static void main(final String[] args) throws IOException {
    final BufferedReader bufferedReader =
        new BufferedReader(
            new InputStreamReader(System.in, java.nio.charset.StandardCharsets.UTF_8));

    final int N = Integer.parseInt(bufferedReader.readLine().trim());

    for (int i = 1; 10 >= i; i++) {
      System.out.printf("%d x %d = %d\n", N, i, N * i);
    }

    bufferedReader.close();
  }
}
