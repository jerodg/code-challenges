int maxDepth(char* s) {
    int max = 0;
    int depth = 0;
    for(int i = 0; s[i] != '\0'; i++) {
        if(s[i] == '(') {
            depth++;
            if(depth > max) {
                max = depth;
            }
        } else if(s[i] == ')') {
            depth--;
        }
    }
    return max;
}