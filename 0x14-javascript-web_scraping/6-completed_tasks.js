#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response, body) {
    if (err) {
        console.log(err);
    } else if (response.statusCode === 200) {
        const completed = {};
        const tasks = JSON.parse(body);
        for (const task in tasks) {
            if (tasks[task].completed === true) {
                if (completed[tasks[task].userId] === undefined) {
                    completed[tasks[task].userId] = 1;
                } else {
                    completed[tasks[task].userId]++;
                }
            }
        }
        console.log(completed);
    } else {
        console.log('An error occured. Status code: ' + response.statusCode);
    }
});