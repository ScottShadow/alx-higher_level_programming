#!/usr/bin/node
const request = require('request');
const charId = "/18/";
request(process.argv[2], function (err, response, body) {
    if (err) {
        console.log(err);
    } else if (response.statusCode === 200) {
        const results = JSON.parse(body).results;
        console.log(results.reduce((count, movie) => {
            return movie.characters.find((actor) => actor.endsWith(charId))
                ? count + 1
                : count;
        }, 0));
    } else {
        console.log('Error code: ' + response.statusCode);
    }
});