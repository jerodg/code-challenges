#include <stdint.h>

/**
 * This function determines the feedback for a hoop jumping exercise based on
 * the number of successful jumps.
 *
 * @param n The number of successful hoop jumps made by the user.
 *
 * @return A string message encouraging the user to either move on to tricks if
 * they've made 10 or more jumps, or to keep practicing if they've made less
 * than 10 jumps.
 */
char *hoop_count(uint32_t n) {
    return n >= 10 ? "Great, now move on to tricks"
                   : "Keep at it until you get it";
}
