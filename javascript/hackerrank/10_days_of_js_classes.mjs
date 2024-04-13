/**
 * Polygon class that calculates the perimeter of a polygon.
 *
 * @property {number[]} sides - The sides of the polygon.
 */
class Polygon {
    /**
     * Constructs a new instance of the Polygon class.
     *
     * @param {number[]} sides - The sides of the polygon.
     */
    constructor(sides) {
        this.sides = sides;
    }

    /**
     * Calculates the perimeter of the polygon.
     *
     * @returns {number} - The perimeter of the polygon.
     */
    perimeter() {
        return this.sides.reduce((a, b) => a + b, 0);
    }
}

// Create a new instance of the Polygon class representing a rectangle
const rectangle = new Polygon([10, 20, 10, 20]);

// Create a new instance of the Polygon class representing a square
const square = new Polygon([10, 10, 10, 10]);

// Create a new instance of the Polygon class representing a pentagon
const pentagon = new Polygon([10, 20, 30, 40, 43]);

// Log the perimeter of the rectangle, square, and pentagon
console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
