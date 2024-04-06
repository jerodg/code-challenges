#include <stdbool.h>

bool isIsomorphic(const char *s, const char *t) {
  char s2t[128] = {0};
  char t2s[128] = {0};
  for (int i = 0; s[i]; i++) {
    if (!s2t[s[i]] && !t2s[t[i]]) {
      s2t[s[i]] = t[i];
      t2s[t[i]] = s[i];
    } else if (s2t[s[i]] != t[i] || t2s[t[i]] != s[i]) {
      return 0;
    }
  }
  return 1;
}
