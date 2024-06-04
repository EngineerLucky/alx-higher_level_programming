#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, res, body) => {
  if (error) console.log(error);
  else {
    JSON.parse(body).characters.forEach(character => {
      request.get(character, (error, res, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    });
  }
});
