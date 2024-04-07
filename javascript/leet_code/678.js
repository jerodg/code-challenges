/**
 * @param {string} s
 * @return {boolean}
 */
let checkValidString = function (s) {
    let left = 0;
    let right = 0;

    for (let i = 0; i < s.length; i++) {
        left += s[i] === "(" ? 1 : -1;
        right += s[i] !== ")" ? 1 : -1;

        if (right < 0) {
            break;
        }

        left = Math.max(left, 0);
    }

    return left === 0;
};
