#!/usr/bin/node
/**
 * class Rectangle - defines a rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Instance method that prints the rectangles using the character 'X'
  print () {
    let x = 0;
    let y = 0;
    let output = '';

    while (x < this.height) {
      while (y < this.width) {
        output += 'X';
        y++;
      }
      console.log(output);
      x++;
    }
  }

  /**
   * Instance method that exchanges the width and the geight of the rectangle
   */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  /**
   * Instance method that multiplies the width and the height of the rectangle by 2
   */
  double () {
    [this.width, this.height] = [2 * this.width, 2 * this.height];
  }
}

module.exports = Rectangle;
