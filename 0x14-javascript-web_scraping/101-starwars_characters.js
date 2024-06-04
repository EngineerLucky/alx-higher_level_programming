#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const urllink = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(urllink, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
// console.log(characters);
	  for (const character of characters) {
      request.get(character, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
