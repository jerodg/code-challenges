/**
 * This script creates a button with an initial value of "0".
 * When the button is clicked, it increments the value by 2.
 */

// Create a new button element
let btn = document.createElement("Button");

// Set the initial inner HTML of the button to "0"
btn.innerHTML = "0";

// Set the id of the button to "btn"
btn.id = "btn";

// Set the class of the button to "btnClass"
btn.className = "btnClass";

// Append the button to the body of the document
document.body.appendChild(btn);

// Add a click event listener to the button
btn.onclick = function () {
    // When the button is clicked, increment the value by 2
    btn.innerHTML = parseInt(btn.innerHTML) + 2;
};
