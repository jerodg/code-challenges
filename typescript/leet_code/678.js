function checkValidString(s) {
    var low = 0;
    var high = 0;
    for (var i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            low++;
            high++;
        }
        else if (s[i] === ")") {
            low = Math.max(low - 1, 0);
            high--;
            if (high < 0) {
                return false;
            }
        }
        else {
            low = Math.max(low - 1, 0);
            high++;
        }
    }
    return low === 0;
}
