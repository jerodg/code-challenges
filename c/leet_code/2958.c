#include <stdio.h>
#include <stdlib.h>

int maxSubarrayLength(int *nums, int numsSize, int k) {
    int left = 0;
    int maxNum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxNum) {
            maxNum = nums[i];
        }
    }
    int *counter = (int *) calloc(maxNum + 1, sizeof(int));
    int max_length = 0;
    for (int right = 0; right < numsSize; right++) {
        counter[nums[right]]++;
        while (counter[nums[right]] > k) {
            counter[nums[left]]--;
            left++;
        }
        max_length = max_length > (right - left + 1) ? max_length : (right - left + 1);
    }
    free(counter);
    return max_length;
}