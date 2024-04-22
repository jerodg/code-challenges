// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>

class Solution {
public:
    void merge(std::vector<int> &nums1, int m, std::vector<int> &nums2, int n) {
        int i = 0, j = 0;
        std::vector<int> result;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                result.push_back(nums1[i]);
                i++;
            } else {
                result.push_back(nums2[j]);
                j++;
            }
        }
        while (i < m) {
            result.push_back(nums1[i]);
            i++;
        }
        while (j < n) {
            result.push_back(nums2[j]);
            j++;
        }
        nums1 = result;

    }
};
