class Solution {
  int timeRequiredToBuy(List<int> tickets, int k) {
    int time = 0;
    int i = 0;
    bool flag = true;
    while (flag) {
      for (int i = 0; i < tickets.length; i++) {
        if (tickets[k] == 0) {
          flag = false;
          break;
        }
        if (tickets[i] == 0) {
        } else {
          tickets[i] = tickets[i] - 1;
          time++;
        }
      }
    }
    return time;
  }
}
