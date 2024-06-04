#!/usr/bin/node
// A script that displays a status code

const request = require('request');

request.get(process.argv[2], (err, res) => {
  if (err) console.log(err);
  else console.log('code: ' + res.statusCode);
});
