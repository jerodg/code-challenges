public class Solution
{
    public int TimeRequiredToBuy(int[] tickets, int k)
    {
        int n = tickets.Length;
        Queue<int> queue = new Queue<int>(tickets);

        int time = 0;

        while (queue.Count > 0)
        {
            int rounds = Math.Min(queue.Count, k);
            for (int i = 0; i < rounds; i++)
            {
                queue.Dequeue();
            }
            time += rounds;
        }
        return time;
    }
}
// fixme: this solution exceeds the time limit