/**
 * @param {string} s
 * @return {string}
 */
let minRemoveToMakeValid = function (s) {
    let stack = [];
    let remove = [];
    for (let i = 0; i < s.length; i++) {
        if ("(" === s[i]) {
            stack.push(i);
        } else if (")" === s[i]) {
            if (0 === stack.length) {
                remove.push(i);
            } else {
                stack.pop();
            }
        }
    }
    stack = stack.concat(remove);
    stack = stack.sort((a, b) => a - b);
    let result = "";
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (j < stack.length && stack[j] === i) {
            j++;
        } else {
            result += s[i];
        }
    }
    return result;
};
