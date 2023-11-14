#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
    charPrint (c) {
      if (!c) {
        c = 'x';
      }
      this.print(c);
    }
 }
 
module.exports = Square;
