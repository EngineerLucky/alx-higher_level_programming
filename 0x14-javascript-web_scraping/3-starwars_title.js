#!/usr/bin/node
// star wars title

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(urllink, (err, res, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
