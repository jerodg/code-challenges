/**
 * This function handles button clicks for a binary calculator.
 * It takes an event object, determines the type of button that was clicked,
 * and performs the appropriate action.
 *
 * @param {Event} e - The event object.
 */
function onButton(e) {
    // Get the button that was clicked
    let btn = e.target;

    // Get the action associated with the button
    let action = document.getElementById(btn.id).innerHTML;

    // Get the result display element
    let res = document.getElementById("res");

    // Perform the appropriate action based on the button that was clicked
    switch (action) {
        case "C":
            // If the button was "C", clear the result display
            res.innerHTML = "";
            break;
        case "=":
            // If the button was "=", evaluate the expression in the result display
            let expr = res.innerHTML;
            let nums = /(\d+)/g;
            // Replace all base 2 nums with base 10 equivs
            expr = expr.replace(nums, function (match) {
                return parseInt(match, 2);
            });
            // eval in base 10 and convert to base 2
            res.innerHTML = eval(expr).toString(2);
            break;
        default:
            // If the button was any other button, append its action to the result display
            res.innerHTML += action;
            break;
    }
}

// Get all the buttons
let buttons = document.getElementsByTagName("button");

// Add the onButton function as a click event handler for each button
for (let button of buttons) {
    button.onclick = onButton;
}
