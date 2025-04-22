document.addEventListener("DOMContentLoaded", function () {
	const characterElement = document.querySelector("#character");
	const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  
	fetch(apiUrl)
	  .then((response) => response.json())
	  .then((data) => {
		characterElement.textContent = data.name;
	  })
	  .catch((error) => {
		console.error("Error fetching data:", error);
	  });
  });
  