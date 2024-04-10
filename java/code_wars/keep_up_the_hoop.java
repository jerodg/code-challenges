/**
 * The HelpAlex class provides a method to determine the feedback message for Alex based on the
 * number of hoops.
 */
public class HelpAlex {

  /**
   * This method returns a feedback message for Alex based on the number of hoops.
   *
   * @param n The number of hoops.
   * @return A string message. If the number of hoops is 10 or more, the message encourages Alex to
   *     move on to tricks. If the number of hoops is less than 10, the message encourages Alex to
   *     keep trying.
   */
  public static String hoopCount(int n) {
    if (n >= 10) {
      return "Great, now move on to tricks";
    } else {
      return "Keep at it until you get it";
    }
  }
}
