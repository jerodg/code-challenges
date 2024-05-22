/// Dart implementation of a hypothetical problem.
///
/// This module contains a class `Solution` with a method `timeRequiredToBuy`.
/// The `timeRequiredToBuy` method takes in two parameters:
/// - `tickets`: A list of integers representing the number of tickets each person has.
/// - `k`: An integer representing the index of the person in the queue.
///
/// The method returns an integer representing the time required for the person at index `k` to buy all their tickets.
/// Each person buys one ticket at a time, and it takes one unit of time to buy a ticket.
/// When a person has bought all their tickets, they leave the queue.
/// The person at index `k` continues to stay in the queue until they have bought all their tickets.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `tickets` is a list of integers and `k` is an integer.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.
library;

class Solution {
  /// Calculates the time required for the person at index `k` to buy all their tickets.
  ///
  /// This method uses a while loop to simulate the process of the people buying tickets.
  /// It iterates until the person at index `k` has bought all their tickets.
  /// In each iteration, it goes through the queue and each person buys one ticket if they still have tickets left.
  /// The time is incremented by one for each ticket bought.
  ///
  /// @param tickets The number of tickets each person has.
  /// @param k The index of the person in the queue.
  /// @return The time required for the person at index `k` to buy all their tickets.
  int timeRequiredToBuy(List<int> tickets, int k) {
    int time = 0;
    bool flag = true;
    while (flag) {
      for (int i = 0; i < tickets.length; i++) {
        // If the person at index `k` has bought all their tickets, stop the process.
        if (tickets[k] == 0) {
          flag = false;
          break;
        }
        // If the current person still has tickets left, they buy one ticket.
        if (tickets[i] > 0) {
          tickets[i]--;
          time++;
        }
      }
    }
    return time;
  }
}
