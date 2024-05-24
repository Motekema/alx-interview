#!/usr/bin/node

const request = require('request');

// Check if a movie ID was provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a request to the Star Wars API for the movie details
request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }

  // Parse the response body to get the list of characters
  const actors = JSON.parse(body).characters;

  // Function to print characters in order
  const exactOrder = (actors, x) => {
    if (x === actors.length) return;

    // Make a request to get each character's details
    request(actors[x], function (err, res, body) {
      if (err) {
        console.error(err);
        return;
      }

      // Print the character's name and proceed to the next character
      console.log(JSON.parse(body).name);
      exactOrder(actors, x + 1);
    });
  };

  // Start printing characters
  exactOrder(actors, 0);
});
