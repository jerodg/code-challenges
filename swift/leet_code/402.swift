/**
 `Solution` class contains the solution for the problem.

 This class has a single method `removeKdigits` which is used to remove `k` digits from the input `num` to get the smallest possible number.
 */
class Solution {
    /**
      This function removes `k` digits from the input `num` to get the smallest possible number.

      - Parameters:
        - num: The original number represented as a string.
        - k: The number of digits to remove.
      - Returns: The smallest possible number after removing `k` digits. If all digits are removed, returns "0".

      The function works by converting the input string to an array of `CChar` for processing. It then iterates over each character in the number, and while there are still digits to remove and the last digit in the stack is greater than the current digit, it removes the last digit from the stack. If there are still digits to remove after this process, it removes them from the end. Finally, it finds the index of the first non-zero digit and returns the number as a string, or "0" if all digits are zero.
     */
    func removeKdigits(_ num: String, _ k: Int) -> String {
        // Convert the input string to an array of CChar for processing
        let na = num.utf8CString
        // Define a zero value for comparison
        let zv = "0".utf8CString
        // If the number of digits to remove is greater than or equal to the number of digits in the input, return "0"
        if k >= na.count - 1 { return "0" }
        // Initialize the number of digits to remove and the stack to hold the digits of the number
        var rem = k, st: [CChar] = []
        // Iterate over each character in the number
        for i in 0 ..< na.count - 1 {
            let e = na[i]
            // While there are still digits to remove and the last digit in the stack is greater than the current digit
            while !st.isEmpty, rem > 0, st.last! > e {
                // Remove the last digit from the stack
                st.removeLast()
                // Decrease the number of digits to remove
                rem -= 1
            }
            // Add the current digit to the stack
            st += [e]
        }
        // If there are still digits to remove, remove them from the end
        for i in 0 ..< rem {
            st.removeLast()
        }
        // Find the index of the first non-zero digit
        let j = st.firstIndex(where: { $0 != zv[0] }) ?? st.count
        // If the index is less than the count of digits in the stack, return the number as a string, otherwise return "0"
        return j < st.count ?st[j...].reduce(into: "") { $0 += String(UnicodeScalar(UInt8($1))) } : "0"
    }
}
