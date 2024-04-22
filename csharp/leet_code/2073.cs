using System.Collections.Generic; // Required for List<>
using System.Linq; // Required for ToList()

/// <summary>
/// Solution class contains methods to solve the problem.
/// </summary>
public class Solution
{
    /// <summary>
    /// Calculates the time required to buy a ticket.
    /// </summary>
    /// <param name="tickets">An array of integers representing the number of tickets available at each counter.</param>
    /// <param name="k">An integer representing the index of the counter where the user is standing.</param>
    /// <returns>An integer representing the time required to buy a ticket.</returns>
    /// <exception cref="System.ArgumentOutOfRangeException">Thrown when 'k' is out of range of 'tickets' array.</exception>
    public int TimeRequiredToBuy(int[] tickets, int k)
    {
        // Convert the array to a list for easier manipulation
        List<int> ticketslist = tickets.ToList();

        // Check if 'k' is within the range of 'tickets' array
        if (k < 0 || k >= ticketslist.Count)
        {
            throw new System.ArgumentOutOfRangeException(nameof(k), "Index is out of range of 'tickets' array.");
        }

        // Counter to keep track of the time
        int counter = 0;

        // Loop until the tickets at the user's counter are not zero
        while (ticketslist[k] != 0)
        {
            // Iterate over all the counters
            for(int i = 0; i < ticketslist.Count; i++)
            {
                // Increment the time counter
                counter++;

                // Decrement the number of tickets at the current counter
                ticketslist[i]--;

                // If the tickets at the current counter are zero
                if (ticketslist[i] == 0)
                {
                    // If the user is at the current counter, break the loop
                    if(k == i)
                    {
                        break;
                    }

                    // Remove the current counter from the list
                    ticketslist.RemoveAt(i);

                    // If the current counter is before the user's counter, decrement the user's counter index
                    if (i < k)
                    {
                        k--;
                    }

                    // Decrement the loop counter to adjust for the removed counter
                    i--;
                }
            }
        }

        // Return the time counter
        return counter;
    }
}
