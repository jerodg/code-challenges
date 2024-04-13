/**
 * Rectangle class
 *
 * @class
 * @param {number} w - The width of the rectangle.
 * @param {number} h - The height of the rectangle.
 */
class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}

/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */

/**
 * Function to calculate the area of the rectangle
 *
 * @returns {number} - The area of the rectangle
 */
Rectangle.prototype.area = function () {
    return this.w * this.h;
};

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */

/**
 * Square class that inherits from Rectangle
 *
 * @class
 * @param {number} s - The side length of the square.
 */
class Square extends Rectangle {
    constructor(s) {
        super(s, s);
    }
}

if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify(["constructor"])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);

    // Log the area of the rectangle and square
    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}
