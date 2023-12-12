#!/usr/bin/node

const a = process.argv[2];

function getFactorial (num) {
  num = parseInt(num);

  if (isNaN(num)) {
    return 1;
  } else if (num <= 0) {
    return 1;
  } else { return num * getFactorial(num - 1); }
}

console.log(getFactorial(a));
