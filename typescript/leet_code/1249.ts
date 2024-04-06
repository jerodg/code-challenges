function minRemoveToMakeValid(s: string): string {
    let stack = [];
    let sArr = s.split("");
    for (let i = 0; i < sArr.length; i++) {
        if (sArr[i] === "(") {
            stack.push(i);
        } else if (sArr[i] === ")") {
            if (stack.length > 0) {
                stack.pop();
            } else {
                sArr[i] = "";
            }
        }
    }
    for (let i = 0; i < stack.length; i++) {
        sArr[stack[i]] = "";
    }
    return sArr.join("");
}
