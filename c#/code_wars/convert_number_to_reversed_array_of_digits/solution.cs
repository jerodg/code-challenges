using System;
using System.Collections.Generic;

namespace Solution
{
  class Digitizer
  {
    public static long[] Digitize(long num)
    {
        // Convert the number to a string
        string numStr = num.ToString();

        // Create an empty list
        List<long> digitList = new List<long>();

        // Iterate over the string in reverse order
        for (int i = numStr.Length - 1; i >= 0; i--)
        {
            // Convert each character to an integer and append to the list
            digitList.Add(long.Parse(numStr[i].ToString()));
        }

        return digitList.ToArray();
    }
  }
}