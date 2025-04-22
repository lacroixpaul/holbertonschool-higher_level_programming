document.addEventListener("DOMContentLoaded", function () {
	const moviesList = document.querySelector("#list_movies");
	const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";
  
	fetch(apiUrl)
	  .then((response) => response.json())
	  .then((data) => {
		data.results.forEach((movie) => {
		  const listItem = document.createElement("li");
		  listItem.textContent = movie.title;
		  moviesList.appendChild(listItem);
		});
	  })
	  .catch((error) => {
		console.error("Error fetching data:", error);
	  });
  });
  