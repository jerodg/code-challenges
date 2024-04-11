using System;
using System.Collections.Generic;
using System.Linq;

class Result
{
    // This function calculates the total number of integers that are between the two sets.
    public static int GetTotalX(List<int> a, List<int> b)
    {
        int count = 0;
        // Loop from the maximum of the first list to the minimum of the second list.
        for (int i = a.Max(); i <= b.Min(); i++)
        {
            // Check if all elements in the first list are factors of i and i is a factor of all elements in the second list.
            if (a.All(x => i % x == 0) && b.All(x => x % i == 0))
            {
                count++;
            }
        }
        return count;
    }
}

class Solution
{
    public static void Main(string[] args)
    {
        // Create a TextWriter object to write the output to a file.
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        // Read the first line of input and split it into an array.
        string[] firstMultipleInput = Console.ReadLine().TrimEnd().Split(' ');

        // Convert the first two elements of the array to integers.
        int n = Convert.ToInt32(firstMultipleInput[0]);
        int m = Convert.ToInt32(firstMultipleInput[1]);

        // Read the second line of input, split it into an array, convert each element to an integer, and store them in a list.
        List<int> arr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(arrTemp => Convert.ToInt32(arrTemp)).ToList();

        // Read the third line of input, split it into an array, convert each element to an integer, and store them in a list.
        List<int> brr = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(brrTemp => Convert.ToInt32(brrTemp)).ToList();

        // Call the GetTotalX function and store the result.
        int total = Result.GetTotalX(arr, brr);

        // Write the result to the file.
        textWriter.WriteLine(total);

        // Flush the buffer and close the TextWriter object.
        textWriter.Flush();
        textWriter.Close();
    }
}