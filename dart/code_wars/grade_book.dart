/// Returns the grade for the given scores.
///
/// This function takes three integer scores as arguments and returns the grade based on the average of the scores. The average is calculated by adding the scores and dividing by 3. The grade is determined as follows:
/// - 'A' for an average of 90 or above
/// - 'B' for an average of 80 or above
/// - 'C' for an average of 70 or above
/// - 'D' for an average of 60 or above
/// - 'F' for an average below 60
///
/// Example:
/// ```dart
/// var result = getGrade(90, 85, 92);
/// print(result);  // Outputs: A
/// ```
///
/// [a]: The first score.
/// [b]: The second score.
/// [c]: The third score.
/// Returns the grade for the given scores.
String getGrade(int a, int b, int c) {
  // Calculating the average of the scores by adding them and dividing by 3.
  var avg = (a + b + c) ~/ 3;

  // Determining the grade based on the average of the scores.
  if (avg >= 90) {
    return 'A';
  } else if (avg >= 80) {
    return 'B';
  } else if (avg >= 70) {
    return 'C';
  } else if (avg >= 60) {
    return 'D';
  } else {
    return 'F';
  }
}
