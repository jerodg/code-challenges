class Solution {
  public void merge(final int[] nums1, final int m, final int[] nums2, final int n) {
    final int[] nums1_copy = new int[m];
    System.arraycopy(nums1, 0, nums1_copy, 0, m);

    int p1 = 0;
    int p2 = 0;
    int p = 0;

    while (p1 < m && p2 < n) {
      if ((nums1_copy[p1] < nums2[p2])) {
        nums1[p++] = nums1_copy[p1++];
      } else {
        nums1[p++] = nums2[p2];
        p2++;
      }
    }

    if (p1 < m) {
      System.arraycopy(nums1_copy, p1, nums1, p1 + p2, m + n - p1 - p2);
    }

    if (p2 < n) {
      System.arraycopy(nums2, p2, nums1, p1 + p2, m + n - p1 - p2);
    }
  }
}
