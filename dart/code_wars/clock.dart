/// Returns the time since midnight in milliseconds.
///
/// This function takes three parameters: hours, minutes, and seconds. It converts these values into milliseconds and returns the sum.
/// There are 60,000 milliseconds in a minute, 3,600,000 milliseconds in an hour, and 1000 milliseconds in a second.
///
/// Example:
/// ```dart
/// var result = past(0, 1, 1);
/// print(result);  // Outputs: 61000
/// ```
///
/// [h]: The hours since midnight.
/// [m]: The minutes since midnight.
/// [s]: The seconds since midnight.
/// Returns the time since midnight in milliseconds.
int past(int h, int m, int s) {
  // Converting hours to milliseconds
  int hoursInMilliseconds = h * 60 * 60 * 1000;
  // Converting minutes to milliseconds
  int minutesInMilliseconds = m * 60 * 1000;
  // Converting seconds to milliseconds
  int secondsInMilliseconds = s * 1000;

  // Returning the sum of hours, minutes, and seconds in milliseconds
  return hoursInMilliseconds + minutesInMilliseconds + secondsInMilliseconds;
}
