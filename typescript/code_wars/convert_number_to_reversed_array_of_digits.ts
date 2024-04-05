export const digitize = (n: number): number[] => {
    // Convert the number to a string
    let numStr: string = n.toString();

    // Create an empty array
    let digitList: number[] = [];

    // Iterate over the string in reverse order
    for (let i: number = numStr.length - 1; i >= 0; i--) {
        // Convert each character to an integer and append to the list
        digitList.push(parseInt(numStr[i]));
    }

    return digitList;
};
