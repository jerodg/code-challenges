impl Solution {
    /// Removes `k` digits from `num` to create the smallest possible number.
    ///
    /// # Arguments
    ///
    /// * `num` - A string representation of the number from which digits are to be removed.
    /// * `k` - The number of digits to remove from `num`.
    ///
    /// # Returns
    ///
    /// * A string representation of the smallest possible number after removing `k` digits.
    pub fn remove_kdigits(num: String, k: i32) -> String {
        // Convert k to usize for compatibility with Vec operations
        let mut k = k as usize;

        // Initialize an empty stack to hold the digits of the number
        let mut stack: Vec<char> = Vec::new();

        // Iterate over each character in the number
        for c in num.chars() {
            // While the stack is not empty, k is greater than 0, and the current character is less than the last character in the stack
            while !stack.is_empty() && k > 0 && c < *stack.last().unwrap() {
                // Remove the last character from the stack and decrement k
                stack.pop();
                k -= 1;
            }

            // Push the current character onto the stack
            stack.push(c);
        }

        // Remove the remaining digits from the end of the number
        for _ in 0..k {
            stack.pop();
        }

        // Convert the stack into a string to construct the smallest possible number
        let mut result = stack.into_iter().collect::<String>();

        // Remove leading zeros from the number
        result = result.trim_start_matches('0').to_string();

        // If the result is an empty string, return "0"
        if result.is_empty() {
            return "0".to_string();
        }

        // Return the smallest possible number as a string
        result
    }
}
