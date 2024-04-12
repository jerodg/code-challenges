"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.digitize = void 0;
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
    return digitList;
};
exports.digitize = digitize;
