/// <summary>
/// The Solution class.
/// </summary>
public class Solution 
{
    /// <summary>
    /// Removes k digits from the input number string to make the number as small as possible.
    /// </summary>
    /// <param name="num">The input number as a string.</param>
    /// <param name="k">The number of digits to remove.</param>
    /// <returns>A string representing the smallest possible number after removing k digits.</returns>
    public string RemoveKdigits(string num, int k) 
    {
        // If k equals the length of the number string, return "0"
        if (k == num.Length) 
        {
            return "0";
        }

        // Initialize a stack to hold the digits of the number
        var stack = new Stack<char>();

        // Iterate over each digit in the number string
        foreach (char digit in num) 
        {
            // While k is greater than 0 and the top of the stack is greater than the current digit
            while (k > 0 && stack.Count > 0 && stack.Peek() > digit) 
            {
                // Pop the top of the stack and decrement k
                stack.Pop();
                k--;
            }

            // Push the current digit onto the stack
            stack.Push(digit);
        }

        // While k is greater than 0, pop the top of the stack and decrement k
        while (k > 0) 
        {
            stack.Pop();
            k--;
        }

        // Convert the stack to an array and reverse it
        char[] resultArray = stack.ToArray();
        Array.Reverse(resultArray);

        // Find the index of the first non-zero digit
        int startIndex = 0;
        while (startIndex < resultArray.Length && resultArray[startIndex] == '0') 
        {
            startIndex++;
        }

        // If all digits are zero, return "0", otherwise return the number string starting from the first non-zero digit
        return startIndex == resultArray.Length ? "0" : new string(resultArray, startIndex, resultArray.Length - startIndex);
    }
}
