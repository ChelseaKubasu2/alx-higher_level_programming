#!/usr/bin/node
/**
 * class Square - defines a square and inherits from Rectangle.
 */
class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
