// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")

#include <unordered_map>
#include <algorithm>
#include <vector>


class Solution {
public:
    int maxSubarrayLength(std::vector<int> &nums, int k) {
        int left = 0;
        std::unordered_map<int, int> counter;
        int max_length = 0;
        for (int right = 0; right < nums.size(); ++right) {
            ++counter[nums[right]];
            while (counter[nums[right]] > k) {
                --counter[nums[left]];
                if (counter[nums[left]] == 0) {
                    counter.erase(nums[left]);
                }
                ++left;
            }
            max_length = std::max(max_length, right - left + 1);
        }
        return max_length;

    }
};
