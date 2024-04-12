/**
 * @param {string} s
 * @return {number}
 */
const maxDepth = function (s) {
    let maxDepth = 0;
    let currentDepth = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            currentDepth++;
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
            }
        } else if (s[i] === ")") {
            currentDepth--;
        }
    }
    return maxDepth;
};
