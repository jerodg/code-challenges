/**
 * The hoopCount function determines the level of proficiency in hula hooping.
 * It takes a number as an argument which represents the number of hoops a user can spin.
 *
 * @param {number} n - The number of hoops a user can spin.
 * @returns {string} - A motivational message based on the user's proficiency.
 * If the user can spin 10 or more hoops, the function returns "Great, now move on to tricks".
 * If the user can spin less than 10 hoops, the function returns "Keep at it until you get it".
 */
const hoopCount = n => {
    // Check if the number of hoops is greater than or equal to 10
    if (10 <= n) {
        // If so, return a message indicating the user is ready for tricks
        return "Great, now move on to tricks";
    }
    // If the number of hoops is less than 10, return a message encouraging the user to keep practicing
    return "Keep at it until you get it";
};
