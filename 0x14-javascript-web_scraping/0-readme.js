#!/usr/bin/node
const fs = require('fs');
file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
    console.log(err || data);
});