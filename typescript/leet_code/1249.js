function minRemoveToMakeValid(s) {
    var stack = [];
    var sArr = s.split("");
    for (var i = 0; i < sArr.length; i++) {
        if (sArr[i] === "(") {
            stack.push(i);
        }
        else if (sArr[i] === ")") {
            if (stack.length > 0) {
                stack.pop();
            }
            else {
                sArr[i] = "";
            }
        }
    }
    for (var i = 0; i < stack.length; i++) {
        sArr[stack[i]] = "";
    }
    return sArr.join("");
}
