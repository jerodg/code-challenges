/**
 * Function to remove duplicates from a sorted array in-place
 * and return the new length of the array.
 *
 * @param {number[]} nums - The sorted array of numbers
 * @returns {number} - The new length of the array
 */
var removeDuplicates = function (nums) {
    // Initialize the index of the first element
    let i = 0;

    // Iterate over the array
    for (let j = 0; j < nums.length; j++) {
        // If the current element is not equal to the element at index i
        if (nums[j] !== nums[i]) {
            // Increment i and update the element at index i
            i++;
            nums[i] = nums[j];
        }
    }

    // Return the new length of the array
    return i + 1;
};
