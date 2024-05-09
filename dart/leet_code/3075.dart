/// Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
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

/// A `Solution` class that provides a method to calculate the maximum happiness sum.
class Solution {
  /// Calculates the maximum happiness sum from a list of happiness values.
  ///
  /// The function sorts the happiness list in ascending order and then iteratively adds the maximum
  /// happiness value to the sum, decreasing the value by the index each time. If the calculated value
  /// is negative, it adds zero to the sum instead. This process is repeated `k` times.
  ///
  /// @param happiness A list of integers representing happiness values.
  /// @param k The number of times to add the maximum happiness value to the sum.
  /// @return The maximum happiness sum as an integer.
  int maximumHappinessSum(List<int> happiness, int k) {
    happiness.sort();
    int sum = 0;
    int index = 0;

    while (k > 0) {
      // Calculate the value to add to the sum. If the value is negative, add zero instead.
      sum += (happiness[happiness.length - index - 1] - index).isNegative
          ? 0
          : (happiness[happiness.length - index - 1] - index);
      k--;
      index++;
    }
    return sum;
  }
}
