/**
 * Function to remove a specific element from an array in-place
 * and return the new length of the array.
 *
 * @param {number[]} nums - The array of numbers
 * @param {number} val - The value to remove
 * @returns {number} - The new length of the array
 */
const removeElement = function (nums, val) {
    // Initialize the index of the first element
    let i = 0;

    // Iterate over the array
    for (let j = 0; j < nums.length; j++) {
        // If the current element is not equal to the value to remove
        if (nums[j] !== val) {
            // Update the element at index i and increment i
            nums[i] = nums[j];
            i++;
        }
    }

    // Return the new length of the array
    return i;
};
