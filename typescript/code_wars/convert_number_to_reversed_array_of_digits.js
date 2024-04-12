"use strict";
/**
 * @fileoverview This module contains a function that converts a number to a reversed array of its digits.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.digitize = void 0;
/**
 * Function to convert a number to a reversed array of its digits.
 * @param {number} n - The number to be converted.
 * @return {number[]} The reversed array of digits.
 */
var digitize = function (n) {
    // Convert the number to a string
    var numStr = n.toString();
    // Create an empty array
    var digitList = [];
    // Iterate over the string in reverse order
    for (var i = numStr.length - 1; i >= 0; i--) {
        // Convert each character to an integer and append to the list
        digitList.push(parseInt(numStr[i]));
    }
    // Return the reversed array of digits
    return digitList;
};
exports.digitize = digitize;
