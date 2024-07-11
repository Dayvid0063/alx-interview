#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const categories = {
  lnk: `https://swapi.dev/api/films/${movieId}/`,
  method: 'GET'
};

request(categories, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    const film = JSON.parse(body);
    printCharacters(film.characters, 0);
  } else {
    console.error('Failed to fetch movie details:', error);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode == 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      printCharacters(characters, index + 1);
    } else {
      console.error('Failed to fetch character details:', error);
    }
  });
}
