#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request(urlPath, function (res) {
  console.log(`code: ${res.statusCode}`);
});
