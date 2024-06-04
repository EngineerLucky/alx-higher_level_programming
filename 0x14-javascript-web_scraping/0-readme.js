#!/usr/bin/node
// Reading from a file
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, result) => {
  if (err) console.log(err);
  else console.log(result);
});
