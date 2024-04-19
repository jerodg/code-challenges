#include <stdbool.h>

bool checkValidString(const char *s) {
    int low = 0, high = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') {
            low++;
            high++;
        } else if (s[i] == ')') {
            low--;
            high--;
        } else {
            low--;
            high++;
        }
        if (high < 0) {
            return false;
        }
        low = low > 0 ? low : 0;
    }
    return low == 0;
}
