function maxDepth(s) {
    var maxDepth = 0;
    var currentDepth = 0;
    for (var i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            currentDepth++;
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
            }
        }
        else if (s[i] === ")") {
            currentDepth--;
        }
    }
    return maxDepth;
}
