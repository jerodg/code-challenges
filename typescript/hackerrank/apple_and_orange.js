process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let inputLines = [];
let currentLine = 0;
process.stdin.on('data', function(inputStdin) {
  inputString += inputStdin;
});
process.stdin.on('end', function() {
  inputLines = inputString.split('\n');
  inputString = '';
  main();
});

function readLine() {
  return inputLines[currentLine++];
}

/**
 * @fileoverview This module contains a solution for the "Apple and Orange" problem from HackerRank.
 * The problem is solved by calculating the positions of the apples and oranges and checking if they fall within the
 *     house's location.
 */
/**
 * Function to count the number of apples and oranges that fall on Sam's house.
 * @param {number} s - The start point of Sam's house.
 * @param {number} t - The end point of Sam's house.
 * @param {number} a - The location of the apple tree.
 * @param {number} b - The location of the orange tree.
 * @param {number[]} apples - The distances at which each apple falls from the tree.
 * @param {number[]} oranges - The distances at which each orange falls from the tree.
 */
function countApplesAndOranges(s, t, a, b, apples, oranges) {
  let appleCount = 0;
  let orangeCount = 0;
  // Calculate the position of each apple and check if it falls on the house
  for (var i = 0; i < apples.length; i++) {
    const apple = apples[i];
    const applePosition = a + apple;
    if (applePosition >= s && applePosition <= t) {
      appleCount++;
    }
  }
  // Calculate the position of each orange and check if it falls on the house
  for (var i = 0; i < oranges.length; i++) {
    const orange = oranges[i];
    const orangePosition = b + orange;
    if (orangePosition >= s && orangePosition <= t) {
      orangeCount++;
    }
  }
  // Print the number of apples and oranges that fall on the house
  console.log(appleCount);
  console.log(orangeCount);
}

function main() {
  const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
  const s = parseInt(firstMultipleInput[0], 10);
  const t = parseInt(firstMultipleInput[1], 10);
  const secondMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
  const a = parseInt(secondMultipleInput[0], 10);
  const b = parseInt(secondMultipleInput[1], 10);
  const thirdMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
  const m = parseInt(thirdMultipleInput[0], 10);
  const n = parseInt(thirdMultipleInput[1], 10);
  const apples = readLine().replace(/\s+$/g, '').split(' ').map(function(applesTemp) {
    return parseInt(applesTemp, 10);
  });
  const oranges = readLine().replace(/\s+$/g, '').split(' ').map(function(orangesTemp) {
    return parseInt(orangesTemp, 10);
  });
  countApplesAndOranges(s, t, a, b, apples, oranges);
}
