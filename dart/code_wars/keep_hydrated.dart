import 'dart:core';

/// Returns the number of litres of water a person should drink in a given amount of time.
///
/// This function takes the time (in hours) a person has been doing a physical activity as an argument and returns the number of litres of water they should drink. The person should drink half a litre of water per hour of activity, so the function divides the time by 2 and rounds down to the nearest whole number.
///
/// Example:
/// ```dart
/// var result = litres(3);
/// print(result);  // Outputs: 1
/// ```
///
/// [time]: The time (in hours) the person has been doing a physical activity.
/// Returns the number of litres of water the person should drink.
int litres(num time) {
  // Dividing the time by 2 and rounding down to the nearest whole number to get the number of litres of water the person should drink.
  return (time / 2).floor();
}
