#!/usr/bin/node

const request = require('request');

// Function to fetch character names in the exact order
const exactOrder = (actors, index) => {
  if (index === actors.length) return; // Base case: if index equals the length of actors array, stop the recursion
  request(actors[index], function (err, res, body) {
    if (err) throw err; // If there's an error, throw the error
    console.log(JSON.parse(body).name); // Parse and print the character's name
    exactOrder(actors, index + 1); // Recursive call to fetch the next character
  });
};

// Check if the Movie ID is provided as an argument
if (process.argv.length > 2) {
  const movieId = process.argv[2]; // Extract the Movie ID from the command line arguments

  // Request the movie details from the Star Wars API using the provided Movie ID
  request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (err, res, body) {
    if (err) throw err; // If there's an error, throw the error
    const actors = JSON.parse(body).characters; // Parse the response body to get the list of character URLs
    exactOrder(actors, 0); // Call the exactOrder function to fetch and print character names in order
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <movie_id>'); // Display usage information if Movie ID is not provided
}
