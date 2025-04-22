document.addEventListener("DOMContentLoaded", function () {
	const helloElement = document.querySelector("#hello");
	const apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  
	fetch(apiUrl)
	  .then((response) => response.json())
	  .then((data) => {
		helloElement.textContent = data.hello;
	  })
	  .catch((error) => {
		console.error("Error fetching data:", error);
	  });
  });
  