/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see SSPL.
 */

/// `Solution` class.
///
/// This class is part of the `leet_code` package and is defined in the `leet_code/1863.dart` file.
/// It contains a method to calculate the sum of all possible XOR subsets of a given list of integers.
class Solution {
  /// Calculates the sum of all possible XOR subsets of a given list of integers.
  ///
  /// This method uses the bitwise OR operator to calculate the XOR of all elements in the list.
  /// The result is then left-shifted by the number of elements in the list minus one.
  ///
  /// The method assumes that the input list `n` is not empty.
  ///
  /// @param n A list of integers. This list should not be empty.
  /// @return The sum of all possible XOR subsets of the list.
  /// @throws ArgumentError If the input list `n` is empty.
  int subsetXORSum(List<int> n) {
    if (n.isEmpty) {
      throw ArgumentError('Input list must not be empty');
    }
    return n.reduce((a, b) => a | b) << (n.length - 1);
  }
}
