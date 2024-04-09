int timeRequiredToBuy(int *tickets, int ticketsSize, int k) {
  int n = 0, t = 0;
  while (tickets[k] > 0) {
    for (int i = 0; i < ticketsSize; i++) {
      if (tickets[i] != 0) {
        tickets[i] -= 1;
        n++;
        if (i == k && tickets[i] == 0)
          return n;
      }
    }
  }
  return n;
}
