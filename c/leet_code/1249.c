char *minRemoveToMakeValid(char *s) {
    int len = strlen(s);
    int stack[len];
    int stack_size = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            stack[stack_size++] = i;
        } else if (s[i] == ')') {
            if (stack_size > 0) {
                stack_size--;
            } else {
                s[i] = '*';
            }
        }
    }
    for (int i = 0; i < stack_size; i++) {
        s[stack[i]] = '*';
    }
    int new_len = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] != '*') {
            s[new_len++] = s[i];
        }
    }
    s[new_len] = '\0';
    return s;
}
