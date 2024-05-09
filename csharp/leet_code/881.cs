/*
Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
*/

/// <summary>
/// The Solution class contains methods to solve the problem of determining the minimum number of rescue boats required.
/// </summary>
public class Solution {
    /// <summary>
    /// Calculates the minimum number of rescue boats required to save all people.
    /// </summary>
    /// <param name="people">An array of integers where each integer represents the weight of a person.</param>
    /// <param name="limit">An integer representing the maximum weight a boat can carry.</param>
    /// <returns>An integer representing the minimum number of boats required.</returns>
    public int NumRescueBoats(int[] people, int limit) {
        // Sort the array of people's weights
        Array.Sort(people);
        int i=0;
        int j=people.Length-1;
        int ans = 0;

        // Iterate through the array from both ends
        while(i <= j )
        {
            // If the sum of the weights of the lightest and heaviest person is less than or equal to the limit, increment i
            if(people[i] + people[j] <= limit)
                i++;

            // Decrement j after each iteration
            j--;
            // Increment the number of boats required
            ans++;
        }
        // Return the minimum number of boats required
        return ans;
    }
}
