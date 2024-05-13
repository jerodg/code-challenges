/// Copyright ©2010-2024 JerodG <https://github.com/jerodg/>
///
/// This program is free software: you can redistribute it and/or modify it under the terms of the
/// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
/// or (at your option) any later version.
///
/// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
/// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
/// for more details.
///
/// The above copyright notice and this permission notice shall be included in all copies or
/// substantial portions of the Software. You should have received a copy of the SSPL along with this
/// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

/// A solution class for solving a specific problem.
///
/// This class provides a method to find the Kth smallest prime fraction from a list of sorted prime numbers.
class Solution {
  /// Finds the Kth smallest prime fraction from a list of sorted prime numbers.
  ///
  /// The method works by using a binary search approach to find the fraction. It starts with a range of 0 to 1
  /// and calculates the middle value. It then counts the number of fractions that are less than or equal to this
  /// middle value and adjusts the range accordingly. The process is repeated until the Kth smallest fraction is found.
  ///
  /// @param A The list of sorted prime numbers.
  /// @param K The rank of the fraction to find.
  /// @return The Kth smallest prime fraction represented as a list of two integers.
  List<int> kthSmallestPrimeFraction(List<int> A, int K) {
    double l = 0, r = 1;
    int p = 0, q = 1;

    for (int n = A.length, cnt = 0; true; cnt = 0, p = 0) {
      double m = (l + r) / 2;

      // Iterate over the list of prime numbers.
      for (int i = 0, j = n - 1; i < n; i++) {
        // Adjust the index j so that A[i] / A[n - 1 - j] <= m.
        while (j >= 0 && A[i] > m * A[n - 1 - j]) j--;

        // Count the number of fractions that are less than or equal to m.
        cnt += (j + 1);

        // Update the fraction if it is larger than the current one.
        if (j >= 0 && p * A[n - 1 - j] < q * A[i]) {
          p = A[i];
          q = A[n - 1 - j];
        }
      }

      // Adjust the range based on the count of fractions.
      if (cnt < K) {
        l = m;
      } else if (cnt > K) {
        r = m;
      } else {
        return [p, q];
      }
    }
  }
}
