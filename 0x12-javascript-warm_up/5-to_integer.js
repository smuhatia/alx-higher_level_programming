#!/usr/bin/node

const firstArgv = process.argv[2];
const num = parseInt(firstArgv);

if (!isNaN(num)) {
	  console.log('My number:', num);
} else {
	  console.log('Not a number');
}
