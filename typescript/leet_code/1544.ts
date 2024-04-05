function makeGood(s: string): string {
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if (stack.length === 0) {
            stack.push(s[i]);
        } else {
            let top = stack[stack.length - 1];
            if (top.toLowerCase() === s[i].toLowerCase() && top !== s[i]) {
                stack.pop();
            } else {
                stack.push(s[i]);
            }
        }
    }
    return stack.join("");
}
