#!/usr/bin/node

const args = process.argv;
const argc = process.argv.length;

if (argc < 4) {
  console.log(0);
} else {
  const array = args.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
