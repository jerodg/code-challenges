function removeElement(nums, val) {
    var i = 0;
    for (var j = 0; j < nums.length; j++) {
        if (nums[j] !== val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
