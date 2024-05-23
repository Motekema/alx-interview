t request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (err, res, body) => {
	  if (err) {
		      console.error('Error:', err);
		      return;
		    }

	  const film = JSON.parse(body);
	  const characters = film.characters;

	  const fetchCharacter = (index) => {
		      if (index >= characters.length) return;

		      request(characters[index], (err, res, body) => {
			            if (err) {
					            console.error('Error:', err);
					            return;
					          }

			            const character = JSON.parse(body);
			            console.log(character.name);
			            fetchCharacter(index + 1);
			          });
		    };

	  fetchCharacter(0);
});
