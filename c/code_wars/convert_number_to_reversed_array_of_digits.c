#include <inttypes.h>
#include <stddef.h>

void digitize(uint64_t n, uint8_t digits[], size_t *length_out) {
    size_t length = 0;
    if (n == 0) {
        digits[length++] = 0;
    } else {
        while (n > 0) {
            digits[length++] = n % 10;
            n /= 10;
        }
    }
    *length_out = length;
}
