/**
 * Function to remove k digits from the input number to get the smallest possible number.
 *
 * @param {string} num - The input number as a string.
 * @param {number} k - The number of digits to remove.
 * @returns {string} - The smallest possible number after removing k digits.
 */
const removeKdigits = function (num, k) {
    // If the number of digits to remove equals the length of the number, return "0"
    if (num.length === k) {
        return "0";
    }

    // Initialize a stack to keep track of the digits
    const stack = [];

    // Iterate over each digit in the number
    for (let i = 0; i < num.length; i++) {
        const current = num[i];

        // While the stack is not empty, the top of the stack is greater than the current digit,
        // and there are still digits to remove, remove the top digit from the stack
        while (stack.length && stack[stack.length - 1] > current && 0 < k) {
            stack.pop();
            k--;
        }

        // Add the current digit to the stack
        stack.push(current);
    }

    // If there are still digits to remove, remove them from the top of the stack
    while (0 < k) {
        stack.pop();
        k--;
    }

    // Remove leading zeros
    while (1 < stack.length && "0" === stack[0]) {
        stack.shift();
    }

    // Return the smallest possible number as a string
    return stack.join("");
};
