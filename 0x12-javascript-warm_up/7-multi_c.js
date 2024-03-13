#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 3) {
  if (typeof argv[2] !== 'number') console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < argv[2]; index++) {
    console.log('C is fun');
  }
}
