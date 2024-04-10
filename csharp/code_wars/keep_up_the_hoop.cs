/// <summary>
/// The Kata class.
/// </summary>
public class Kata
{
    /// <summary>
    /// Determines the encouragement message based on the number of hoops.
    /// </summary>
    /// <param name="n">The number of hoops.</param>
    /// <returns>A string message encouraging the user.</returns>
    public static string HoopCount(int n)
    {
        // If the number of hoops is 10 or more, return a message to move on to tricks
        if (n >= 10)
        {
            return "Great, now move on to tricks";
        }
        // If the number of hoops is less than 10, return a message to keep trying
        else
        {
            return "Keep at it until you get it";
        }
    }
}