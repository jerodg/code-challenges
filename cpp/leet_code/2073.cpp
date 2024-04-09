class Solution {
public:
  int timeRequiredToBuy(vector<int>& ts, int k) {
    int res = 0, target = ts[k];
    // parsing the queue up to k, included
    for (int i = 0; i <= k; i++) {
      // getting the minimum between the current value and target
      res += min(ts[i], target);
    }
    // parsing the queue up from  k, excluded
    target--;
    for (int i = k + 1, lmt = ts.size(); i < lmt; i++) {
      // getting the minimum between the current value and target
      res += min(ts[i], target);
    }
    return res;
  }
};
