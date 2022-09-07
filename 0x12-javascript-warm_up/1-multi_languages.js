#!/usr/bin/node
// Script that prints 3 lines.
const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

lines.forEach(print);

function print (line) {
  console.log(line);
}
