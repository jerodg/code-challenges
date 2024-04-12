/**
 * The hoopCount function determines the level of proficiency in hula hooping.
 * It takes a number as an argument which represents the number of hoops a user can spin.
 *
 * @param {number} n - The number of hoops a user can spin.
 * @returns {string} - A motivational message based on the user's proficiency.
 * If the user can spin 10 or more hoops, the function returns "Great, now move on to tricks".
 * If the user can spin less than 10 hoops, the function returns "Keep at it until you get it".
 */
function hoopCount(n) {
    if (n >= 10) {
        return "Great, now move on to tricks";
    }
    return "Keep at it until you get it";
}
