// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <climits>
#include <vector>

// The Solution class contains a method to solve the problem.
class Solution {
public:
  // The trap method calculates the total amount of water that can be trapped.
  //
  // This method uses two pointers, one from the start (left) and one from the
  // end (right). It also keeps track of the maximum height from the left and
  // right (lmax and rmax). The idea is to move the pointers towards each other
  // and at each step, update the maximum heights and the total water trapped.
  //
  // The total water trapped at a certain position is the minimum of the maximum
  // heights from both sides, minus the height at that position. This is because
  // the water level at a certain position can at most be the minimum of the
  // maximum heights (as water would spill over the lower side), and the amount
  // of water is then the water level minus the height at that position.
  //
  // @param h A vector of integers representing the heights.
  // @return The total amount of water that can be trapped.
  int trap(std::vector<int> &h) {
    int l = 0, r = h.size() - 1, lmax = INT_MIN, rmax = INT_MIN, ans = 0;
    while (l < r) {
      lmax = std::max(lmax, h[l]);
      rmax = std::max(rmax, h[r]);
      ans += (lmax < rmax) ? lmax - h[l++] : rmax - h[r--];
    }
    return ans;
  }
};
