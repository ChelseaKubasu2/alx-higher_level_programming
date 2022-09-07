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
}

module.exports = Rectangle;
