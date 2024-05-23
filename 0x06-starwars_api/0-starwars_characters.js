#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersNamePromises = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
            return;
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      })
    );

    Promise.all(charactersNamePromises)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr));
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
}
