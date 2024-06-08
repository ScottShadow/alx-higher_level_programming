#!/usr/bin/node
const request = require("request");
const fs = require("fs");
const URL = process.argv[2];
file = process.argv[3];
request(URL, function (err, response, body) {
    fs.writeFile(file, body, 'utf8', function (err) {
        if (err) console.log(err);
    })
})