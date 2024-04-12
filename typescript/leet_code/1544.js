function makeGood(s) {
    var stack = [];
    for (var i = 0; i < s.length; i++) {
        if (stack.length === 0) {
            stack.push(s[i]);
        }
        else {
            var top_1 = stack[stack.length - 1];
            if (top_1.toLowerCase() === s[i].toLowerCase() && top_1 !== s[i]) {
                stack.pop();
            }
            else {
                stack.push(s[i]);
            }
        }
    }
    return stack.join("");
}
