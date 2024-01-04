#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request(urlPath, function(err, res, body) {
    console.log(res);
});

